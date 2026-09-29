# Voice Diary MVP

A private, local-first daily journal workflow for iPhone Voice Memos. The MVP uses Apple Shortcuts to find today's recordings, transcribe them, organize each distinct thought or event with a controlled tag, and save one Markdown daily note in an Obsidian vault.

No personal recordings or transcripts belong in this repository. The example content is synthetic.

## MVP flow

1. Record naturally in Apple's Voice Memos. Keep one thought per recording when convenient; do not rename recordings just for the workflow.
2. Run the `Daily Voice Diary` shortcut (first manually, then optionally from a daily time automation).
3. The shortcut finds recordings created today, transcribes each, and passes the transcripts to the organizer prompt.
4. The organizer returns Markdown with one tagged bullet per distinct item.
5. Save or append the result to `Daily Voice Diary/YYYY-MM-DD.md` in the Obsidian vault.

The exact iOS action availability varies by version. See [`shortcuts/SETUP.md`](shortcuts/SETUP.md) and validate the flow manually before enabling a schedule.

## Taxonomy

The controlled vocabulary lives in [`config/tags.json`](config/tags.json). Each item gets one primary domain tag, at most one related domain tag, and optional facet tags. Do not invent synonyms or new tags during summarization. Use `#review` when the category is genuinely unclear.

## Organizer prompt

Use [`prompts/organize-zh.md`](prompts/organize-zh.md) as the prompt for the Shortcuts `Use Model` action. It requires faithful extraction, no calorie/medical/psychological inference, chronology, and consistent tags.

## Example

[`examples/2026-09-29.md`](examples/2026-09-29.md) shows the intended note format using invented content.

