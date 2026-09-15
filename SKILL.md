---
name: feishu-photography-shoot-plan
description: Research photography references and create compact shoot plans delivered as either a Feishu document or a verified PDF, with shot boards, camera and model guidance, and an uncropped source gallery. Use for photography reference collection, imitation-shoot planning, or refining an existing plan. Do not use for single-image critique or image generation alone.
---

# Photography Shoot Plan

Produce beautiful reference images with concise, executable shooting guidance. Let the user choose one delivery format: a Feishu document or a directly generated PDF. Do not create both unless requested. The established default layout is two 3×4 shot boards for 24 shots plus a separate source gallery; an explicit new brief overrides it.

## Route the work

- Use `photography-shoot-planner` to audit shot-size coverage, pose diversity, model direction, shooting order, and safety.
- Use browser or web research only when references must be collected. Preserve the canonical post URL, creator, and work title whenever available.
- For Feishu delivery, use `lark-doc` to read, create, or edit the document and locate embedded whiteboard tokens; use `lark-whiteboard` to create, inspect, update, export, and verify each board.
- For PDF delivery, use `pdf:pdf` to generate, render, inspect, and verify the final PDF. Follow that skill's artifact-operation and output requirements.
- Use this skill as the orchestration layer. The referenced skills remain authoritative for their own tools and permissions.

## Choose delivery and operation modes

- Establish `delivery_format` as `feishu` or `pdf` before producing the deliverable. If the user has not chosen, ask one short question because the choice changes tools, permissions, output, and verification. Do not silently default to Feishu.
- **New plan:** collect or ingest references, create the local source folder and shot plan, build the chosen deliverable, then verify it.
- **Update plan:** inspect the existing Feishu document or PDF, preserve the source or a backup, change only the requested images, copy, or layout, then verify the result in the same format unless conversion was requested.
- If the user asks only for aesthetic criticism or one generated image, stop using this skill and route to the narrower capability.

## Establish the brief

- Capture the delivery format, theme, target image count, column count, reference source, required shot sizes, props, location, lighting direction, safety constraints, and whether the target is new or existing.
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

## Build the deliverable

- Keep images dominant, gaps narrow, and copy readable at the intended viewing size. Each shot board has an internal title such as “主题 · 摄影参考 01–12”; the source section has “主题 · 摄影参考来源” plus verified source and image counts.
- Put everything needed to understand a board in the deliverable itself: title, shot numbers, guidance, and source attribution. Do not rely on chat prose to complete it.
- For Feishu delivery, read [references/whiteboard-layout.md](references/whiteboard-layout.md), preview new boards locally, then follow the live whiteboard update workflow.
- For PDF delivery, read [references/pdf-layout.md](references/pdf-layout.md), generate the PDF directly from the validated plan and source manifest, and do not create or mutate Feishu content.

## Verify the result

- In either format, verify expected image count, one image per shot card, required guidance, grid, continuous numbering, source order, original aspect ratios, attribution, and internal titles.
- For Feishu, re-export every live board, inspect raw nodes and preview, confirm document order and tokens, and retain the pre-edit export until verification passes.
- For PDF, reopen the final file, verify page count and text structure, render every page to images, and inspect both page overview and card-detail legibility. A successful PDF write or text extraction alone is insufficient.
- For text-only updates, confirm images and their geometry are unchanged.

## Stop conditions

- Do not fabricate missing source links, creator names, original capture settings, or safety facts.
- If there are too few distinct references, report the coverage gap instead of repeating images to reach a number.
- If Feishu authentication or edit permission is missing, follow the relevant Lark skill's minimum-permission flow and pause for user authorization. This does not block PDF delivery when the user chose PDF.
- Do not publish, message, or share the final document or PDF beyond the target explicitly authorized by the user.

## Completion criteria

- The plan passes structural validation with no errors.
- The final reference set covers the requested shot sizes and has intentional variation rather than cosmetic repetition.
- Every card has a unique image reference, concise technical guidance, and an executable model cue.
- Risky shots have actionable boundaries or cancellation conditions.
- The chosen deliverable is compact and independently understandable, and its format-specific structure and rendering have been checked. Source photographs remain uncropped independent images, with strong unselected works included when available.
