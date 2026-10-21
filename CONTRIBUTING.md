# Contributing to Expert Roles

Suggest experts or changes through [issues](https://github.com/shpoont/expert-roles/issues).

## Expert selection

This is a broad expert catalogue.

Use the [project definition](README.md#who-is-included). Assess the person's
expertise, suitability as an AI perspective and contribution to the collection
separately:

- **Evidence of expertise:** substantial research, creations, professional
  results or demonstrated mastery, supported by reliable public sources.
  Check what each source establishes and seek independent corroboration where
  available. Formal credentials are optional.
- **Accessible approach:** public work reveals useful methods, assumptions
  or trade-offs. Identify the perspective through books, articles, talks,
  research or documented practice; prominence and content volume alone do not
  establish it.
- **Task fit and scope:** show relevant uses and the limits of the person's
  documented expertise. Consider what remains applicable when using historical
  work, and keep editorial interpretations distinguishable from documented ideas.
- **Collection contribution:** compare neighboring experts. Prefer useful gaps,
  complementary approaches and overlap that supports meaningful comparison.
  Review coverage against relevant work and subfields, rather than equal counts
  per group. Initial selection priorities can differ from expert eligibility.
- **Faithful use:** public familiarity within the field helps these lightweight
  roles rely on model knowledge, but does not establish faithful or useful
  outputs. Record material uncertainty; claims of role benefit need task-level
  evidence separate from profile or file validation.

Living and historical experts can qualify. Keep the introduction, references,
specialties and suggested uses concise; no detailed expert brief is needed.
Add an optional `perspective` phrase when specialties alone leave a useful
distinction unclear, grounded in linked public work. Keep it nonexhaustive and
describe the expert's emphasis; the assignment supplies the activities.

## Adding an expert

1. Copy the entire [starter folder](src/templates/profile/), including
   `README.md` and `expert.yaml`, using a unique lowercase, hyphenated name.

   ```sh
   cp -R src/templates/profile src/roles/your-expert
   ```

2. Fill `expert.yaml` and the profile README: name, specialties, a short
   introduction, suggested uses and public references. Choose shared IDs from
   [specialties.yaml](src/specialties.yaml) using the
   [specialty rules](docs/elements/specialties.md#rules); propose an entry if needed.
   Add `perspective` where useful, following the
   [metadata guide](src/README.md#role-metadata-and-descriptions).
3. Use a permitted `portrait.jpg` or create a `placeholder.svg` placeholder using
   the [exact image instructions](src/README.md#choose-the-profile-image).
   Photos need attribution, terms, edits and a **Source** link. Placeholders need
   an **Image** section identifying the placeholder.
4. Run the [generator and checks](src/README.md#generate-the-catalogue-and-native-files),
   then review the catalogue, profile and links. Replace every unfilled `{{...}}`
   field and include source changes and regenerated outputs in the pull request.

Record meaningful changes under **Unreleased** in [CHANGELOG.md](CHANGELOG.md).
Maintainers assign the release version using the [release guide](docs/delivery.md#versions-and-releases).

## Profile image

Require exactly one square visual: a photo named `portrait.jpg`, or a
`placeholder.svg` made from the [shared template](src/templates/placeholder.svg).
Use the expert's full name from `expert.yaml`; the command handles line breaks
and type size automatically.
Photos are preferred when suitable and permitted; their absence does not block
an expert. Display either visual at **160 × 160** in the catalogue and
**240 × 240** on the profile. Follow the linked image instructions to switch.

## Photo standard

For photos: **512 × 512 pixels, RGB JPEG**, named `portrait.jpg`. Use a clear
crop of the expert's face and shoulders. Placeholders use the template's 512 × 512
SVG canvas and consistent styling.

## Photo sources and licenses

Start with the expert's Wikipedia biography and follow the portrait to its file
page. Look for alternatives on [Wikimedia Commons](https://commons.wikimedia.org/),
[Openverse](https://openverse.org/) and
[Flickr Creative Commons](https://www.flickr.com/creativecommons/). For historical
experts, also try the [Smithsonian's portrait collection](https://npg.si.edu/portraits),
[Library of Congress](https://www.loc.gov/free-to-use/) and
[NYPL Digital Collections](https://digitalcollections.nypl.org/), using their
Open Access or public-domain filters. Verify terms on the original file page.

**Accept any photo with verified free reuse permission, with or without an
attribution requirement. Always include attribution.** Public-domain / CC0,
[CC BY](https://creativecommons.org/licenses/by/4.0/) and
[CC BY-SA](https://creativecommons.org/licenses/by-sa/4.0/) are examples;
other licenses and clear custom reuse statements can also qualify.

The terms must permit the actual catalogue use and required image preparation.
Record and follow any conditions. Assess limits on commercial use or edits
against the planned use, rather than rejecting a license category automatically.
A clear existing grant supplies permission without a separate request.
**If permission is missing or unclear, do not use the image.**

Public visibility on Wikipedia, LinkedIn, an official profile or a publisher's
site does not grant reuse permission. Wikipedia also hosts non-free images;
check the individual file's terms, not the article's text license.

- Always credit the available creator, title and source, even when attribution
  is optional. Record the license and version or other reuse permission, link
  its terms, and retain required credits, notices and earlier edit history.
- Describe our crop, resize and other changes. For CC BY-SA, keep the modified
  portrait under the same license; the library's own license is separate. Do not
  impose additional restrictions on reuse of the photo.
- Do not imply the photographer or expert endorses this project. Check the
  specific photo's terms; a website's general license may exclude its images.

## Profile sources

`README.md` holds the profile and image note or photo credit; `expert.yaml`
holds the name, specialty IDs and optional `perspective`. Native files under
`dist/codex/` and `dist/claude/`, all three distribution indexes and both catalogue
entry points' marked sections are generated. Edit sources and regenerate;
include source changes and updated outputs together. Both hosts
use the same description and all experts use the shared execution instruction.

Submit original contributions under [MIT](LICENSE), and only contribute material
you have the right to license. Portraits retain their individually credited
licenses. The SVG template and original name placeholders use MIT. Preserve
the [vocabulary source credits](docs/elements/specialties.md#source-attribution)
when copying referenced terms.
