# PDF Layout

Read only when `delivery_format` is `pdf`. The PDF is the final deliverable, not an export placeholder for a Feishu document.

## Structure

- Use the same validated `shot-plan.json` and source manifest as the Feishu route.
- For the 24-shot default, use two consecutive 3×4 shot-board pages numbered 01–12 and 13–24, followed by source-gallery pages. Do not add a separate cover unless requested.
- For other counts, use at most 12 shot cards per page and allow the final page to be shorter. Do not pad with duplicate or weak images.
- Keep each page independently understandable with an internal theme title. Source-gallery pages include the verified source count, image count, creator, work title, and readable canonical URL.
- Use at most four independent full images per source-gallery row. Preserve source order, original aspect ratio, and the complete photograph; never stretch images or crop limbs to fill a slot.
- Do not add introductory essays, execution-reminder pages, a duplicate source table, or decorative filler unless explicitly requested. Use unnumbered headings and unordered lists for requested supporting prose.

## Page design

- Choose a page size and orientation that keeps the requested grid readable at the intended screen or print size. Preserve the 3-column default unless the user requests another column count or readability requires fewer columns.
- Keep the photograph dominant at roughly 65–75% of each shot card. Place the two-digit number and short title below it, followed by separate `机位｜`, `光线｜`, and `口令｜` lines.
- Use consistent card widths, typography, margins, gutters, and theme colors across pages. Measure wrapped text; do not shrink type merely to force a card onto the page.
- Embed a font that covers all Chinese and Latin characters. Missing glyphs, tofu boxes, clipped text, overlapping elements, and low-contrast captions are release blockers.
- Keep source URLs human-readable and clickable when the PDF generator supports link annotations.

## Generation

- Follow `pdf:pdf`, including its required artifact-operation marker immediately before the first authoring command.
- Prefer a deterministic generator such as ReportLab. Write one stable, descriptive final PDF and keep intermediate assets separate from the delivered file.
- Build from the original reference images rather than screenshots of a Feishu board. Do not recompress images more than necessary for a practical file size.

## Verification

- Reopen the final PDF and confirm it is readable, has the expected page count, and contains continuous shot IDs with no missing or duplicate cards.
- Extract text to check titles, `机位｜`, `光线｜`, `口令｜`, source attribution, and URLs, but do not treat extraction as visual proof.
- Render every page to PNG and inspect the full page plus representative card-detail crops. Verify image clarity, aspect ratios, text wrapping, margins, contrast, and source-gallery ordering.
- Confirm one image per shot card, at most four source images per row, and no blank, clipped, stretched, or unexpectedly rotated pages.
- Deliver only the final PDF. Do not cite or expose rendered previews and scratch files unless requested.
