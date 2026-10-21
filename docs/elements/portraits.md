# Profile portraits

The adopted **studio-v1** style uses a new professional studio sitting,
**direct eye contact**, faithful apparent age and facial characteristics, and a
**different moderately muted background for each expert**. Keep one visual per
profile: `portrait.jpg` or the standard full-name `placeholder.svg`.

The method reproduces the inputs, prompt, background recipe and preparation.
AI generation is variable: identical pixels are not guaranteed, and the built-in
tool does not expose a fixed seed or necessarily a model identifier.

## Choose eligible references

Use only photographic subjects supported by reliably attributed photographs
whose reuse terms permit the planned use. Follow the
[photo policy](../../CONTRIBUTING.md#photo-sources-and-licenses).

- Keep drawings, paintings, engravings, statues and similar depictions in their
  original form with existing credits. Do not generate replacements for them.
- Retain a photograph or full-name placeholder when references are absent,
  insufficient for likeness, or their permission is unclear. Name-only generation
  does not qualify under this method.
- Prefer two or three clear complementary views from a similar period when
  available. This is a practical starting point, not a proven optimal count.
  A good single photograph may suffice. A crop and its full original are one
  photographic reference; frames from one video are not independent photographs.
- Identify the target in a wider group photo. Prefer the original resolution;
  preserve the original file, the permitted face crop and their source credits.
  A tiny or obscured face does not become verified detail through generation.
- Keep an extra photographic source outside the generation inputs for human
  comparison when one is available. Preserve monochrome appearance when color
  would be invented.

## Create a reproducible recipe

The versioned [shared prompt](../../src/templates/portrait.txt) is the single
source for the studio brief. The local [helper](../../src/portraits.py) creates
its per-expert recipe; it does not contact a model, download references or install
roles. Use the project's [Python dependencies](../../src/README.md#generate-the-catalogue-and-native-files).

Download permitted references into a review folder outside the public repository,
then run from the repository root, replacing the example paths:

```sh
python src/portraits.py recipe martin-fowler \
  --reference ../portrait-review/references/fowler-front.jpg \
  --reference ../portrait-review/references/fowler-side.jpg \
  --output ../portrait-review/martin-fowler/recipe.json
```

The record includes the expert's name, exact prompt, template hash, reference-file
hashes and dimensions, background palette and flow, style version and JPEG
preparation settings. Record the actual tool/model and output hashes after the
run. Keep reference files, recipes, exact correction prompts, generated masters,
previous images and selection notes outside the public tree. Recipes contain
local paths and the helper refuses to write them inside this repository.

Use `--appearance-note` for a source-specific constraint, such as preserving a
particular reference's apparent age or not treating glasses held in a hand as
worn eyewear. It belongs to the image recipe, not the expert's role instructions.

### Individual backgrounds

Each expert gets three coordinated colors and a soft flowing gradient. Use the
middle ground between bright candy pastels and nearly monochrome mineral gray:
visible but restrained color, light-to-medium tones and gentle contrast. Avoid
rainbows, neon, scenery, busy bands, logos and bright silhouette halos.

The helper derives a stable palette and flow from `studio-v1`, the canonical
expert slug and an explicit variant number. This is an input-design seed, not
an image-model seed. The three adopted sample palettes are pinned in the helper.
Other experts get their own palette; adding a new expert does not reassign
existing ones. Compare the results together. If two backgrounds look too similar,
try `--background-variant 1` for one expert, increment if needed and record the
chosen number. Do not use
one selected sample's background as a catalogue-wide template.

## Generate and review

1. Attach the recipe's reference files in their recorded order to the available
   built-in image generation tool and use the exact `prompt` value. Record a
   model identifier only when the tool exposes it; otherwise say **not disclosed**.
2. Generate a candidate and compare it with the photographs. Check face shape,
   apparent age, eyes, nose, mouth, jaw, hairline, beard, glasses and individual
   asymmetry separately from lighting or polish. A different background alone
   does not satisfy the studio-sitting brief.
3. Require relaxed **direct eye contact** with the camera. Shoulders may turn
   slightly; head and gaze must stay comfortable. Reject crossed or misaligned
   eyes, distorted glasses, strained sideways gaze and invented facial geometry.
4. Make a targeted correction only when needed, using the accepted candidate as
   the edit target. Lock the person and everything outside the intended change.
   Save that input, the exact correction prompt and its output as a separate step.
   Recheck identity and eye contact after every correction. Do not chain edits
   merely for variety; reuse an already accepted sample when suitable.
5. Inspect the candidate at full resolution and at **160 × 160** catalogue and
   **240 × 240** profile sizes, then compare backgrounds across the collection.
   Reject uncertain likenesses, excessive retouching and visible artifacts.
   Retain the original image or placeholder when the result is unsupported or
   the tool blocks output. Record what was retained and why.

Visual inspection is editorial comparison, not biometric identity verification.
The owner reviews likeness and presentation separately from passing file checks.

## Prepare and credit the image

Back up the previous image and credit before replacement. Keep the original
resolution generated master, then prepare the selected output deterministically:

```sh
python src/portraits.py prepare ../portrait-review/martin-fowler/master.png \
  --output src/roles/martin-fowler/portrait.jpg --replace
```

The helper applies EXIF orientation, a centered square crop, Lanczos resizing,
RGB conversion and JPEG encoding at quality 95 with chroma subsampling disabled.
The result is **512 × 512 RGB JPEG**. It preserves the master and refuses to
replace an existing output without `--replace`. Recipe records include the
installed Pillow version; the project's dependencies pin it.

Start with the [copyable Image credit block](../../src/templates/portrait-credit/README.md).
Replace every placeholder, copy style/variant/palette/flow from the recipe and
repeat the reference entries for every supplied photograph or video. Put linked
terms or an explicit public-domain notice after each **Source** entry, repeating
shared terms when needed; one reference's status does not cover another. Use explicit
**Tool**, **Created** (YYYY-MM-DD), **Model**, **Method** and **Changes** fields.
Use **not disclosed** when the tool does not expose a model identifier. Replace
the existing hero image's filename and accessible text as instructed in the block.

Generated profiles use an **Image** section and matching accessible image text:

- A visible **AI-generated portrait** label and synthetic-likeness disclosure.
- Style `studio-v1`, background variant, palette and flow; link to this method.
- Actual tool, date, method and model identifier when exposed. Describe any
  targeted edits and reuse of an accepted sample accurately.
- **Source** links for every supplied reference, available creators and titles,
  exact licenses or permission terms, earlier edits and the generation changes.
- Applicable adaptation terms, including share-alike or noncommercial conditions.
  Do not automatically relabel a licensed-reference adaptation as MIT.

Keep the public profile self-contained; local reference paths and run records
stay outside the repository. Original generated contributions use the project's
MIT license to the extent rights can be granted. The public-domain status of a
reference is separate from the license of a new generated contribution.
Photographs keep their **Photo credit** sections; historical visuals retain their
credits and **Historical depiction** label; placeholders keep their standard
**Image** note and MIT template credit. Do not imply endorsement.

### Source credits and AI generation

Always retain supplied-reference credits and source terms as project provenance,
including for public-domain references. Whether a generated result is legally
an adaptation depends on the actual reuse and applicable law; supplying an input
does not automatically transfer its license to every output. See the
[Creative Commons adaptation guidance](https://creativecommons.org/faq/#when-is-my-use-considered-an-adaptation).

Generation does not automatically clear source rights. Keep applicable duties
when a source is reused or adapted, including attribution, change notices,
share-alike or noncommercial conditions. This catalogue conservatively retains
the documented source conditions for its reference-based adaptations; do not
remove them merely because the output is generated or has a new background.
Record the basis and scope of the output terms separately from the reference
terms. This is project policy, not a claim that every reference-based output is
legally an adaptation.

Do not claim that an AI output necessarily has its own copyright. A license can
only cover rights the contributor can grant; unrestricted material stays
unrestricted. [Creative Commons guidance on AI outputs](https://creativecommons.org/2023/08/18/understanding-cc-licenses-and-generative-ai/)
distinguishes a human creative contribution from a potentially uncopyrightable
generated portion.

## Keep the generation record

Save `run.json` beside `recipe.json`, outside the public repository. Use the
following minimum fields, replacing every example value with the actual run
data. Master dimensions are an observation, not a required generation size.

```json
{
  "tool": "actual built-in image tool",
  "model": "not disclosed",
  "created": "YYYY-MM-DD",
  "calls": 1,
  "call_file": "imagegen-call-01.json",
  "corrections": [],
  "accepted_sample_reuse": false,
  "template_sha256": "actual template hash from the recipe",
  "master": "master-01.png",
  "master_sha256": "actual SHA-256 of the selected master",
  "portrait_sha256": "actual SHA-256 of the prepared JPEG",
  "master_dimensions": [1254, 1254],
  "master_mode": "RGB",
  "portrait_dimensions": [512, 512],
  "portrait_mode": "RGB",
  "portrait_format": "JPEG"
}
```

Keep the exact, unchanged tool arguments in `call_file`, including the prompt
and ordered references. For multiple calls, also retain an ordered `call_files`
list. Count all calls, including corrections; each correction entry identifies
its input, exact argument file, output and output hash. Record reused accepted
samples accurately. Derive hashes from the saved master and prepared JPEG,
rather than inventing or copying them. From the repository root, replacing
the example paths:

```sh
shasum -a 256 ../portrait-review/martin-fowler/master.png \
  src/roles/martin-fowler/portrait.jpg
```

Keep selection decisions and separate likeness, gaze and background observations
in `decisions.md` under the review folder, and link it from the run report. It
may live alongside `run.json` or at the review folder's root.

## Review a rendered preview

Use an available Markdown previewer or local renderer that supports the raw
HTML used by profiles and catalogue tables. Preview-tool choice is permitted;
no particular renderer is part of the studio-v1 method. Record the actual tool,
commands and observed results with the run artifacts.

Keep generated HTML and other preview artifacts outside the public tree, with
image and navigation paths resolving to the reviewed copy. Open the profile
and catalogue, verify that the actual images load at 240 and 160 pixels, and
inspect the rendered credit, labels and layout. Compare backgrounds together
using the existing portraits; a temporary overview belongs outside the public
tree. Save screenshots when available and distinguish visual inspection from
DOM readback. If no renderer is available, report preview verification as
blocked; passing file checks does not replace it. Local rendering does not
establish hosted GitHub behavior or owner acceptance.

## Verify the change

Run the [generator and checks](../../src/README.md#generate-the-catalogue-and-native-files).
Review generated-image labels, source terms, links, active images, the complete
diff and rendered catalogue. Preserve biographies, expert metadata, specialties,
shared role instructions and native Codex and Claude bytes during portrait-only
work. Check that all experts have an explicit generated-or-retained outcome.
Report rejected or unsupported replacements separately from successful file checks.

The normal generator and its read-only **--check** path validate the generated
Image block, accessible hero label, style/variant/palette/flow, tool/date/model,
method, changes and linked output/reference terms before any export writes.
They reject stale generated credits on a placeholder and missing portrait credit
sections. CI runs this same path. These checks inspect declared metadata, not
the truth of a license claim or a visual likeness. Source permissions, completeness
of supplied-reference credits and visual quality still need review.

The [fresh-session walkthrough](../../tests/portrait-walkthrough.md) tests whether
an independent agent can follow this workflow without the author's conversation.
Its result is separate from automated contract tests.
