# {{name}}

<!-- Copy this folder to src/roles/<person-slug>/, replace every {{...}} field
and remove the authoring notes. Links to native files resolve after generation.
Choose the person using the
[expert selection criteria](../../../CONTRIBUTING.md#expert-selection).
After filling expert.yaml, create placeholder.svg using the command in
[the image guide](../../README.md#choose-the-profile-image).
Use a permitted portrait.jpg instead when available, following that guide.
-->

<img src="placeholder.svg" alt="{{name}} — name placeholder" width="240" height="240">

<!-- Choose task-relevant specialties using docs/elements/specialties.md.
Use one linked canonical label per specialty, separated by a middle dot.
Match expert.yaml and the specialty registry. Link to #specialty-<canonical-id>;
the target remains stable when its label or group changes. -->
[{{specialty_name}}](../README.md#specialty-{{specialty_id}})

<!-- Keep the introduction to one or two sentences: who the person is and what
they are known for. Support it with the public references below; suggested uses
and specialties establish when their perspective is useful. If specialties
overlap, add a short, supported perspective phrase in expert.yaml; it need not
be copied here. -->
{{short_introduction}}

[Codex role file](codex/expert-{{slug}}.toml) ·
[Claude Code role file](claude/expert-{{slug}}.md) ·
[Setup guide](../../../docs/delivery.md#use-a-native-role).

An independent AI perspective inspired by public work; it does not represent
{{name}}.

## Suggested uses

- {{suggested_use_1}}
- {{suggested_use_2}}

## Explore the work

- [Public work]({{public_work_url}}).

## Image

Full-name placeholder, created from the
[shared SVG template](../../templates/placeholder.svg). Original project artwork
under [MIT](../../../LICENSE).

<!-- If using a photograph, change the image filename and alt text above,
then replace this Image section with Photo credit. Record the creator, title,
exact license/version or other permission terms, required notices and edits,
and labeled Source and License links. Always retain attribution. Verify that
the terms permit the actual use and image preparation; do not include an image
with missing or unclear permission. See CONTRIBUTING.md#photo-sources-and-licenses.
Remove this note and the other authoring notes when complete. -->

<details>
<summary>Source files</summary>

[Expert metadata](expert.yaml) ·
[Shared instruction](../../templates/invocation.md)

</details>

[Back to the catalogue](../../roles/README.md)
