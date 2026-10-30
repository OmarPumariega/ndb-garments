// OCR de etiquetas: lista el texto que ve macOS Vision en cada imagen.
// Uso: swiftc -O tools/ocr_labels.swift -o /tmp/ocr_labels && /tmp/ocr_labels img1.jpg img2.jpg ...
import Foundation
import Vision
import AppKit

var cropDir: String? = ProcessInfo.processInfo.environment["OCR_CROPS"]
var currentName = ""
var cropN = 0
func saveCrop(_ cg: CGImage, _ o: VNRecognizedTextObservation) {
    guard let dir = cropDir else { return }
    let b = o.boundingBox
    let W = CGFloat(cg.width), H = CGFloat(cg.height)
    var r = CGRect(x: b.minX * W - 0.15 * b.width * W, y: (1 - b.maxY) * H - 0.6 * b.height * H,
                   width: b.width * W * 1.3, height: b.height * H * 2.2)
    r = r.intersection(CGRect(x: 0, y: 0, width: W, height: H))
    guard let c = cg.cropping(to: r) else { return }
    let rep = NSBitmapImageRep(cgImage: c)
    cropN += 1
    try? rep.representation(using: .png, properties: [:])?.write(to: URL(fileURLWithPath: "\(dir)/\(currentName)__\(cropN).png"))
}
func recognize(_ cg: CGImage) -> [String] {
    var out: [String] = []
    let req = VNRecognizeTextRequest { r, _ in
        for o in (r.results as? [VNRecognizedTextObservation]) ?? [] {
            for c in o.topCandidates(3) { out.append(c.string) }
            if let t = o.topCandidates(1).first?.string.uppercased(), t.contains("EBLAS") || t.contains("IDEB") { saveCrop(cg, o) }
        }
    }
    req.recognitionLevel = .accurate
    req.usesLanguageCorrection = false
    req.minimumTextHeight = 0.004
    try? VNImageRequestHandler(cgImage: cg, options: [:]).perform([req])
    return out
}

func upscaled(_ cg: CGImage, _ f: Int) -> CGImage? {
    let w = cg.width * f, h = cg.height * f
    guard let ctx = CGContext(data: nil, width: w, height: h, bitsPerComponent: 8, bytesPerRow: 0,
        space: CGColorSpaceCreateDeviceRGB(), bitmapInfo: CGImageAlphaInfo.premultipliedLast.rawValue) else { return nil }
    ctx.interpolationQuality = .high
    ctx.draw(cg, in: CGRect(x: 0, y: 0, width: w, height: h))
    return ctx.makeImage()
}

for path in CommandLine.arguments.dropFirst() {
    guard let img = NSImage(contentsOfFile: path),
          let cg = img.cgImage(forProposedRect: nil, context: nil, hints: nil) else { print("\(path)\tERROR"); continue }
    currentName = URL(fileURLWithPath: path).deletingPathExtension().lastPathComponent
    var texts = recognize(cg)
    if let up = upscaled(cg, 2) { texts += recognize(up) }
    let up = texts.map { $0.uppercased().filter { $0.isLetter } }
    let ok = up.contains { $0.contains("NIDEBLAS") }
    let bad = up.filter { $0.count >= 6 && $0.hasSuffix("EBLAS") && !$0.contains("NIDEBLAS") }
    print("\(ok ? "OK " : "NO ")\t\(path)\t\(bad.isEmpty ? "" : "SOSPECHOSO: " + Set(bad).joined(separator: ","))")
}
