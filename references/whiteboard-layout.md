# Whiteboard Layout

Read before creating a board or changing its geometry. These are the user's established defaults; explicit layout requests override them.

## Grid

- For 24 shots, use two 3-column × 4-row shot boards, numbered 01–12 and 13–24, followed by one source-gallery board. For other counts, use at most 12 shots per board and allow the final board to be shorter; do not pad with duplicate or weak images.
- Keep the document to its title, the shot boards, an optional single “参考来源” heading, and the source board. Do not prepend descriptive paragraphs or add a separate execution-reminder section.
- Use one photograph per shot card. Preserve the original image ratio and key pose / costume / environment information; never stretch the image or crop limbs to fill a slot.
- Order the main plan from environment to detail when no stronger production constraint exists. The source gallery follows original source order instead.

## Card hierarchy

- Image area is the dominant element and should occupy roughly 65–75% of the card height.
- Place the two-digit number and short shot title immediately below the image.
- Follow with `机位｜`, `光线｜`, and `口令｜` on separate lines.
- Keep card copy left-aligned. Use consistent labels and font sizes across all cards.
- Prefer a title under 14 Chinese characters. Allow one or two natural lines for model cues; no clipped text or isolated final character. Treat camera settings as proposed reproduction instructions unless verified as original metadata.
- As a practical starting point, keep `camera_line` within 46 display cells, `light_line` within 50, and `cue_line` within 54. The validator reports longer lines for review.
- Fold a brief character adaptation or necessary risk-specific alternative into the card. Reserve extra height only where its content requires it; avoid large blank text panels.
- Use the same card width, palette, type hierarchy, and gap scale across the shot boards. Set text height from measured wrapping. Practical gap: 2–4% of card width; outer margin: 4–6%. Treat these as starting values, not reasons to crop an image.

## Board hierarchy

- Each board must carry its own theme and purpose in a compact internal header. Examples: “奥黛塔 · 摄影参考 01–12”, “奥黛塔 · 摄影参考 13–24”, and “奥黛塔 · 摄影参考来源”. Source / image counts belong in the source-board header and must be computed from the manifest.
- Use one header per board. Avoid row section bars, decorative footers, repeated source headings, and large outside margins. A full-board overview is for scanning; do not shrink text to claim the whole board's copy is readable on a phone at fit-to-screen scale.
- Use restrained theme colors derived from the subject. Contrast and readability take priority over decorative styling.
- Inspect actual exported contrast, especially light text on dark headers, rather than relying on SVG colors alone.
- Keep necessary shot-specific cancellation rules on the relevant card. Do not add a generic plan-wide safety footer or document callout by default.
- Read [source-gallery.md](source-gallery.md) when building or changing the source board. It uses up to four independent full images per row. Attribution and its “摄影参考来源” title must be inside the canvas, because exported images do not include document headings or preserve clickable links.

## New-board workflow

- Create the shot plan and pass validation before rendering.
- The plan's `rows` describes the logical whole selection; splitting into boards does not restart IDs or change selected images.
- Render a local preview and inspect it at both full-board and card-detail scale.
- Check for text overflow, accidental cropping, inconsistent gutters, repeated images, and misleading section labels.
- Write the verified artifact using the workflow required by `lark-whiteboard`.

## Existing-board workflow

- Resolve the embedded board token through `lark-doc`.
- Export `source`, `raw`, and `preview` before editing.
- For copy-only changes, patch the exact raw text nodes and preserve image tokens, coordinates, dimensions, and unrelated text.
- For image replacement or geometry changes, use the SVG editing route from `lark-whiteboard`; retain a pre-edit raw backup.
- Reuse the maintained generator and original files when available. If native image nodes are needed, convert the layout first and replace only image placeholders using measured positions, original aspect ratios, and target-board media tokens.
- Use overwrite only when the chosen whiteboard workflow requires rebuilding the board and the user has authorized that target.

## Live verification

- Re-export raw nodes after the write.
- Confirm the expected count of images, titles, camera lines, light lines, and cue lines.
- A 24-shot default must have exactly 12 images per main board, with continuous IDs across the two boards. Source cards need attribution, not camera / light / cue lines.
- Compare image tokens and image geometry before and after a copy-only edit.
- A new header may require a uniform vertical shift; verify relative image layout and ratios are preserved.
- Confirm no legacy or duplicate labels remain.
- Check source image IDs and count, original ratios, no cropping during asset preparation, source order, creator labels, links, internal title, and at most four images per row.
- Confirm intended document board order. Remove replaced source tables / prose only after their replacement board is verified.
- Export a preview for visual review. Local SVG photos can render while the live board shows placeholders. If the preview service returns a cached image, check live raw state and retry preview after a short delay. Do not call an old preview proof of the new design or repeatedly overwrite to refresh a cache.
- Retain the backup until all structural and visual checks pass.
