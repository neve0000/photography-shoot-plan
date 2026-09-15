# Source Gallery

Read when collecting source material or creating / editing the source board.

## Selection and attribution

- Keep a manifest with source URL, creator, work title, and ordered images. Each image needs a stable ID, original local path, original width / height, and optionally its selected shot IDs and target-board media token.
- Group by the original post and preserve the established group order and within-post image order. Several strong photos from a series are useful even if only one entered the main shot plan.
- Include excellent unselected works already collected. Omit weak, unfinished, backstage, accidental, duplicate, or collage images. The source gallery is not capped at 24 pictures and does not inherit the selected-shot validator's per-source diversity warning.
- Use the actual source link acquired from the creator post. Preserve a verified working full link when stripping parameters produces a QR-only or inaccessible page. Do not invent access tokens or promise links are openable without checking. Visible work titles and creator names remain necessary because static image exports have no clickable links.

## Four-column independent photographs

- Flatten the ordered source groups into consecutive individual image cards, at most four per row. Each photograph is its own full-size card; never turn a source's multiple images into a 2×2 collage inside one card.
- Continue filling the row when a source has only one image. Do not allocate a separate row or a full-width heading to each single-image source. A series may cross a row boundary while remaining contiguous.
- Caption every image with a consistent source ID, work title, and creator. For a multi-image source, add its position, such as `03 · 2/4`; for a single image, use only the source ID. The same source ID and title make a series recognizable across row boundaries.
- Keep captions short and borders / gaps narrow. No camera or model-direction copy is needed on this board. Use an internal title “主题 · 摄影参考来源” and computed counts such as “24 个来源 · 33 幅作品”.
- Original framing takes priority over filling a rectangular slot. Use `scale = min(slot_width / original_width, slot_height / original_height)` and set the image node's actual width / height to the scaled original dimensions. Center it within the slot; modest empty space around a landscape image is preferable to losing its composition.
- Preserve the complete underlying image too: no square crop, `sips -c`, cover / slice operation, or stretching during preprocessing. File-format conversion is allowed while retaining full dimensions. `preserveAspectRatio="xMidYMid meet"` alone cannot undo an already-cropped uploaded asset.

## Feishu rendering lessons

- Upload complete images to the target whiteboard and retain a reusable media map. If a format such as WebP does not render reliably, convert the original to PNG or JPEG without cropping, then upload that complete file.
- SVG conversion can yield `svg` placeholders with zero dimensions instead of native photo nodes. If this occurs, replace those placeholders with native image nodes using the manifest's exact geometry and target-board media tokens. Verify every image has nonzero dimensions and the expected original aspect ratio.
- Keep the canvas background below cards, images above card backgrounds, and captions above other shapes. Stray group ownership or incorrect stacking can produce an almost blank live export.
- Conversion may duplicate linked text nodes at identical positions. Deduplicate identical text / coordinates while retaining rich-link metadata. Keep link targets in native rich text when supported, and verify visible attribution independently.
- Preserve a raw backup and original image manifest before replacing the source board. Verify all image IDs, order, ratios, captions, header, and live rendering after writing. Do not trust success status or a local preview as evidence that the live board contains full photographs.
