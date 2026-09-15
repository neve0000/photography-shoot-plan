---
name: feishu-photography-shoot-plan
description: Research photography references and create compact Feishu shoot-plan documents with mobile-friendly three-column shot boards, camera and model guidance, and a separate uncropped four-column source gallery. Use for photography reference collection, imitation-shoot planning, or creating and refining Feishu photography boards. Do not use for single-image critique or image generation alone.
---

# Feishu Photography Shoot Plan

Produce beautiful reference images with concise, executable shooting guidance. Each whiteboard must make sense when exported as a standalone image. The user's established default is a compact document with two 3×4 shot boards for 24 shots and one separate source-gallery board; an explicit new brief overrides these defaults.

## Route the work

- Use `photography-shoot-planner` to audit shot-size coverage, pose diversity, model direction, shooting order, and safety.
- Use browser or web research only when references must be collected. Preserve the canonical post URL, creator, and work title whenever available.
- Use `lark-doc` to read, create, or edit the Feishu document and to locate embedded whiteboard tokens.
- Use `lark-whiteboard` to create, inspect, update, export, and verify the board. Follow its required authentication and update workflow rather than recreating Feishu API calls here.
- Use this skill as the orchestration layer. The referenced skills remain authoritative for their own tools and permissions.

## Choose a mode

- **New plan:** collect or ingest references, create the local source folder, create a Feishu document with the required shot boards and source board, then verify the live result.
- **Update plan:** read the target document and board, export a backup, change only the requested images, copy, or layout, then verify the live result.
- If the user asks only for aesthetic criticism or one generated image, stop using this skill and route to the narrower capability.

## Establish the brief

- Capture the theme, target image count, column count, reference source, required shot sizes, props, location, lighting direction, safety constraints, and whether the target is new or existing.
- Ask only for missing choices that materially change the result. If unspecified, use three columns and up to four rows per shot board. A 24-shot / 3×8 brief means two consecutive 3×4 boards by default; use a single 3×8 canvas only when explicitly requested. Preserve continuous numbering across boards.
- Treat models as adults unless the user explicitly provides a different lawful, non-sexual context. Never infer consent to publish or commercially reuse source images.

## Build the reference set

- Prefer user-provided images and links, then canonical creator posts, then broader search results.
- Store the final image, canonical source URL, creator, and work title together. Do not use screenshot search-result pages as the canonical source when the original post is available.
- Select for meaningful differences in shot size, posture, direction, energy, camera height, lighting, and background. Do not fill the board with near-duplicates.
- For a beautiful / atmospheric brief, judge the finished photograph first: composition, lighting, expression, pose, and visible detail. Prefer strong finished photographs of the requested character; use excellent other-character, dance, portrait, or fashion photographs for transferable poses when exact-character matches are weaker. Explain the adaptation on the relevant shot card. Do not fill slots with mediocre exact-character matches, backstage pictures, screenshots, or collages.
- One source post may contribute multiple frames when they serve different shot roles, but avoid letting a single post dominate the plan.
- Keep a source manifest including strong collected works that did not enter the final shot selection. Present them on the source board according to [references/source-gallery.md](references/source-gallery.md), filtering out weak or unfinished images. Preserve source and within-source order.

## Create the shot plan

- Before writing the plan, read [references/shot-plan-schema.md](references/shot-plan-schema.md).
- Represent the selected shots in `shot-plan.json`. Keep one image per card.
- Each card uses three short, operational lines:
  - `机位｜` camera height, angle, shot size when useful, and focal length.
  - `光线｜` light direction or quality plus the decisive exposure or composition control.
  - `口令｜` a speakable action sequence for feet or weight, torso or shoulders, hands, gaze, timing, and hold or reset as relevant.
- Include the shutter moment for movement, splash, fabric, or hair actions. Where a real execution risk matters, include a concise substitution or cancellation condition on that shot card. Do not add a generic “现场执行提醒” section or a standalone safety callout by default.
- Camera and lighting settings are proposed reproduction instructions unless source metadata verifies the original settings; do not present estimates as the source photographer's EXIF.
- Run the validator before layout:

```bash
python3 <skill-dir>/scripts/validate_plan.py <path-to-shot-plan.json>
```

- Fix all errors. Treat warnings as review prompts; do not silence them by duplicating images or deleting useful safety detail.

## Build the board and document

- Before rendering or changing layout, read [references/whiteboard-layout.md](references/whiteboard-layout.md).
- Keep images dominant, gaps narrow, and copy readable when a card is enlarged on a phone. A full-board overview is for scanning; do not promise that tiny copy is readable at fit-to-screen scale.
- The default document contains only its title, the consecutive shot boards, an optional single “参考来源” heading, and the source board. No introductory descriptions, per-source document headings, usage notes, execution-reminder section, or native source table. If extra prose is explicitly requested, use unordered lists for long supporting text and unnumbered headings.
- Each shot board has an internal title such as “主题 · 摄影参考 01–12”; the source board has “主题 · 摄影参考来源” plus verified source / image counts. Put all information needed to understand an exported image inside its board, including titles, shot numbers, guidance, and source attribution.
- For a new board, preview locally before writing to Feishu.
- For an existing board, export `source`, `raw`, and `preview` first. Use raw-node editing for text-only changes. Use the whiteboard SVG edit workflow when images or geometry change.
- Generate one idempotent token per logical board update and reuse it only for retries of that same update.

## Verify the live result

- Re-export every live board after writing. For shot boards, verify expected image count, one image per card, guidance, grid, and continuous numbering. For the source board, verify one full image per card, at most four cards per row, source order, original aspect ratios, attribution, and its internal title.
- For text-only edits, confirm image tokens and image geometry are unchanged.
- Confirm document board order and tokens, and that no obsolete prose or duplicate source table remains when the user requested the compact structure. Verify replacement boards before deleting old document blocks.
- A successful write or local image preview alone is insufficient to claim live visual success. Verify live raw nodes and export preview. If the preview is cached, avoid rewriting the board merely to refresh it; allow a short delay and export again. If still stale, state exactly which checks passed and that live visual verification is pending.
- Keep the pre-edit raw export until verification passes. Restore it if the live structure is incomplete or corrupted.

## Stop conditions

- Do not fabricate missing source links, creator names, original capture settings, or safety facts.
- If there are too few distinct references, report the coverage gap instead of repeating images to reach a number.
- If authentication or edit permission is missing, follow the relevant Lark skill's minimum-permission flow and pause for user authorization.
- Do not publish, message, or share the final document beyond the target explicitly authorized by the user.

## Completion criteria

- The plan passes structural validation with no errors.
- The final reference set covers the requested shot sizes and has intentional variation rather than cosmetic repetition.
- Every card has a unique image reference, concise technical guidance, and an executable model cue.
- Risky shots have actionable boundaries or cancellation conditions.
- The Feishu document is compact, all boards are independently understandable as exported images, and live structure and rendering have been checked. Source photographs remain uncropped independent images, with strong unselected works included when available.
