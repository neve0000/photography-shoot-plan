# Shot Plan Schema

Read this reference before creating or validating `shot-plan.json`.

## Root object

- `title` — non-empty project or board title.
- `columns` — positive integer. Use `3` by default.
- `rows` — optional positive integer for the complete logical shot selection, not the height of each exported board. When present, `rows × columns` must equal the number of shots. A 24-shot plan uses `columns: 3, rows: 8` in data and normally renders as two 3×4 boards with IDs 01–12 and 13–24.
- `theme` — optional concise visual thesis.
- `references_collected_online` — optional boolean. Set to `true` when the plan was researched online so missing canonical source URLs are reported.
- `safety_notes` — optional list of plan-wide safety notes.
- `shots` — non-empty ordered list of card objects.

## Card object

- `id` — sequential two-digit string beginning with `01`.
- `section` — row or shot-family label, such as `环境全景`, `动态全身`, or `近景特写`.
- `title` — short action or composition name.
- `image` — unique local path, Feishu image token, or stable media identifier.
- `source_url` — canonical source URL when the image was collected online.
- `source_creator` — optional creator name.
- `source_title` — optional original work title.
- `shot_size` — one of the useful plan labels: `环境`, `全身`, `动态全身`, `七分身`, `中景`, `低位`, `半身`, `近景`, `特写`, or `细节`.
- `camera_line` — card line beginning with `机位｜`.
- `light_line` — card line beginning with `光线｜`.
- `cue_line` — card line beginning with `口令｜`.
- `risk_tags` — optional list such as `wet-surface`, `water`, `unstable-support`, `sharp-prop`, `traffic`, or `height`.
- `cancel_condition` — required in practice when `risk_tags` is non-empty; state the observable condition that stops or simplifies the action.

## Example

This is a complete three-shot schema example. For 24 shots, supply all 24 objects and set `rows` to 8; do not validate a truncated excerpt as a complete plan.

```json
{
  "title": "海边泳装｜姿势与景别参考",
  "columns": 3,
  "rows": 1,
  "theme": "清透蓝调、环境到特写、以可执行姿势为主",
  "safety_notes": [
    "湿滑区域准备防滑垫和协助人员"
  ],
  "shots": [
    {
      "id": "01",
      "section": "环境全景",
      "title": "海景横构图",
      "image": "画板图片/01_海景横构图.webp",
      "source_url": "https://example.com/original-post",
      "source_creator": "示例作者",
      "source_title": "示例作品",
      "shot_size": "环境",
      "camera_line": "机位｜腰高平拍 · 24–35mm",
      "light_line": "光线｜侧逆光；地平线放上三分之一",
      "cue_line": "口令｜坐稳—腿斜伸—看海；浪退时连拍",
      "risk_tags": ["wet-surface", "water"],
      "cancel_condition": "浪势超过脚踝或支撑手打滑时停止"
    },
    {
      "id": "02", "section": "全身", "title": "岸边回望",
      "image": "画板图片/02_岸边回望.webp",
      "source_url": "https://example.com/second-post",
      "shot_size": "全身",
      "camera_line": "机位｜腰高平拍 · 50mm",
      "light_line": "光线｜侧逆光；面部轻补光",
      "cue_line": "口令｜重心后移—转肩—回望—停"
    },
    {
      "id": "03", "section": "近景", "title": "侧脸迎光",
      "image": "画板图片/03_侧脸迎光.webp",
      "source_url": "https://example.com/third-post",
      "shot_size": "近景",
      "camera_line": "机位｜眼平近拍 · 85mm",
      "light_line": "光线｜柔和侧光；眼神光清楚",
      "cue_line": "口令｜肩放松—脸转向光—轻呼气"
    }
  ]
}
```

## Coverage audit

- Order the sequence from easier, wider, and more stable actions toward tighter or more demanding actions unless the location or light requires another order.
- For plans with at least 12 cards, aim to cover at least four of these families: environment, full body, medium or half body, close-up or detail, and movement.
- Separate visually similar cards by changing at least one consequential dimension: subject scale, camera height, body direction, energy, light, or background.
- A row label is not evidence of coverage. Judge the actual image and action.

## Model cues

- Make cues speakable in one breath.
- Prefer a sequence using `—`: base or weight → torso or shoulders → hands → gaze → shutter moment.
- State the hold, reset, or cancellation instruction when it prevents ambiguity or risk.
- Avoid emotional adjectives without physical behavior. Replace “更有气场” with an observable action such as “肩下沉—下巴微收—视线越过镜头”.

## Source rules

- Use the original post URL rather than a search-result page when possible.
- Multiple frames from one post are allowed only when they serve different shot roles.
- Missing source information is a warning for local user-owned material and a defect for newly collected online references.
- The source-gallery manifest is separate from this selected-shot schema. It may contain additional strong works, multiple frames per source, and an incomplete last row in its four-column layout; do not run the shot-card grid validator on it.
