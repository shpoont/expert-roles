# Specialties

## Purpose

Specialties help people and AI match tasks to suitable experts and give the
catalogue a common, predictable structure. A person may know the problem they
want help with without knowing which expert to choose.

The [project agreement](../../PROJECT.md) establishes that purpose. The rules
below turn it into contributor guidance. The central YAML registry is adopted
for the catalogue, and the initial assignments follow these rules.
The vocabulary can grow through the same process.

Coverage reviews identify work and subfields needing useful perspectives across
the broad expert catalogue. They do not change canonical specialty meanings or
establish an expert's eligibility or role value. Compare useful approaches
rather than equal counts per group.

## Rules

1. **Choose for task relevance.** Assign specialties that describe areas where
   the expert's public work is useful. The profile's references and suggested
   uses should support the choice; a detailed expert brief is unnecessary.
2. **Use the shared vocabulary.** Reuse one canonical entry for the same concept
   across all experts. Each entry has a stable identifier, a readable name and
   consistent grouping. Spelling variants and synonyms belong to that concept,
   rather than becoming competing entries.
3. **Describe fields and recognizable approaches.** Both a broad field such as
   Project management and a specific approach such as Critical Chain project
   management can help selection. Generic activities such as reviewing,
   planning or implementing belong in the task, rather than serving as specialties.
4. **Allow useful overlap.** An expert can have several specialties, and a
   specialty can have several experts. Include broad and specific terms when
   each helps task matching. Avoid padding the list with incidental biography
   or every topic the person has ever discussed.
5. **Use established terminology accurately.** Start with an accurate
   [ESCO knowledge concept](https://esco.ec.europa.eu/en/classification/skill).
   If ESCO has no suitable concept, use an appropriate
   [Wikidata concept](https://www.wikidata.org/wiki/Property:P101).
   Check the meaning, not just the label. Prefer a precise Wikidata concept to
   a broader or adjacent ESCO term that changes the intended specialty.
6. **Keep names natural and meaning stable.** Use a source's preferred label or
   a recognized alias. Record the source URL and concept identifier when
   mapping a term. External identifiers describe the specialty; assigning it
   to an expert is this collection's editorial judgment. A label correction
   can retain its ID; a change of meaning needs an explicit vocabulary change.
7. **Review genuine gaps.** If neither reference source fits, propose a new
   shared entry with a short definition, a suitable group and a supporting
   public reference. Check existing entries and aliases first. A separate
   specialist brief or new contribution process is not required.
8. **Use groups for predictable navigation.** Reuse existing broad groups when
   they fit and group each canonical specialty consistently across experts.
   Propose changes to grouping centrally. An external source's hierarchy is
   useful evidence, but does not automatically become this catalogue's layout.

Specialties guide expert selection and the initial perspective; they are not
an exhaustive account of expertise. The expert's documented work defines the
professional scope. Roles decline work outside that scope, separate relevant
parts of mixed requests and clarify uncertain fit or essential missing context.
They challenge unsupported premises, forced conclusions and suppression of
relevant expert judgment while respecting legitimate constraints and contrary
evidence. The task and evidence determine the focus within that expertise.

## Vocabulary scope

Use the larger reference vocabularies when selecting specialties. Keep the
local vocabulary focused on concepts used by this collection. The README
should present specialties with assigned experts, rather than thousands of
empty categories. Aliases should resolve to the canonical entry.

ESCO and Wikidata supply reference concepts for one project vocabulary.
Contributors should not independently choose conflicting names or groups for
the same concept. Preserve source attribution and applicable terms if reference
data is later copied into the repository.

## Current implementation

[src/specialties.yaml](../../src/specialties.yaml) contains 92 mapped entries.
Each has exactly three required fields:

- `name`: the common display label, using a preferred source term or recognized alias.
- `group`: the catalogue navigation group, shared by every use of that entry.
- `reference`: the specific ESCO or Wikidata concept URL, including its external
  ID, or a documented rule-7 primary-source concept page when neither fits.

Each expert's `expert.yaml` lists canonical local IDs. The exporter resolves
those IDs into catalogue labels, native role descriptions and the shared
instruction. It rejects unknown IDs, duplicate names or concept references,
missing fields and malformed reference URLs before writing outputs. It does
not access the network or inject source URLs into role instructions.

An optional `perspective` phrase can clarify a distinctive emphasis when
experts share specialties. It is editorial selection guidance grounded in
public work, not another controlled vocabulary or an exhaustive boundary.
See the [metadata guide](../../src/README.md#role-metadata-and-descriptions).
The phrase contributes only to the generated description; generic activities
remain part of the assignment and execution behavior stays in the shared instruction.

Animal behavior, Computing, Design, Engineering, Finance, Law, Management,
Marketing, Medicine, Philosophy, Psychology, Sales and Systems science are the
current navigation groups. Specialty
rows are sorted by name within each group; unassigned terms and empty groups
are not displayed. Profiles list their most useful specialties first.

### Mapping history

Formal methods and Concurrent computing use Wikidata's field concepts
(Q1049183 and Q128392) under Computing. ESCO search returned activities such as
Verify formal ICT specifications and Use concurrent programming; these do not
describe the intended fields and are not substituted for them.

System dynamics and Systems thinking use Wikidata's field concepts (Q598451
and Q1340474) in the Systems science navigation group. ESCO's Systems
thinking entry is explicitly scoped to a logistic system; it is not substituted
for the broader systems approach used here. System dynamics search results did
not supply the intended field.

System safety and Systems engineering use Wikidata concepts Q7663745 and
Q682496 in the Engineering navigation group. The former concerns
systems-based hazard identification and control; ESCO's broader Safety
engineering entry emphasizes standards and laws and is not substituted for it.
Systems engineering search results did not supply the intended lifecycle field.

General surgery uses ESCO's medical specialty d62c361a-d772-4009-a6c3-cfc10e5a51f1.
Health services research and Patient safety use Wikidata concepts Q2518253 and
Q1475557; ESCO searches primarily returned activities or adjacent subjects.
The Medicine navigation group keeps the clinical and health-services
scope explicit; these labels do not imply expertise in every operational domain.

The notes below retain the sequence of vocabulary additions, including the
profiles that were pending at each earlier step. All accepted profiles are now
complete; the current totals and schema are stated above.

Interaction design uses ESCO's recognized alias for Software interaction design.
The provisional `usability-evaluation` entry is replaced with
`usability-engineering`; the broader discipline is an explicit new assignment,
not a synonym migration. Shared Human-computer interaction tags provide overlap
across the design experts, while specific approaches preserve useful distinctions.
Source labels and recognized aliases are reviewed when choosing a canonical
name; separate alias fields and deeper hierarchy are not needed for these entries.

D017 adds Artificial intelligence, Machine learning, Deep learning and Large
language models under Computing. Their precise Wikidata concepts describe the
fields used by the two completed AI profiles. ESCO's Principles of artificial
intelligence and Utilise machine learning are not treated as interchangeable
labels for the broader fields; its search did not supply suitable knowledge
concepts for Deep learning or Large language models. Large language models uses
a recognized plural alias of the source label. Each assignment is supported
by the expert's linked research, teaching or public work. Huyen's D017 draft
used the same vocabulary; D020 completes her profile with the existing Machine
learning and Large language models assignments. No new concept is required.

D018 adds twenty-one concepts for twelve further completed profiles. ESCO's
Entrepreneurship, Copyright legislation, Marketing management, Distributed
computing and Statistical process control were verified as knowledge concepts.
Precise Wikidata concepts cover the other specific software,
entrepreneurship, quality, finance and technology-law fields and methods.
Adjacent ESCO activities or narrower procedures are not substituted for those
concepts. The registry retains all fourteen earlier entries and adds only terms
used by completed profiles; proposed terms for pending profiles are not imported.
Finance, Law and Marketing provide additional broad navigation groups, while
entrepreneurship and quality concepts reuse Management. Grouping and assignment
remain editorial choices. This expansion changes neither the schema nor the
shared instruction.

D019 adds eight used concepts for five further profiles: Causal inference,
Bayesian networks, Typography, Graphic design, Security engineering, Cyber
security, Brand management and Brand equity. Graphic design and Cyber security
use verified ESCO knowledge concepts. The other six use precise Wikidata
concepts; Bayesian networks is a recognized plural alias. ESCO's Typography
definition is limited to arranging text for printing, so Wikidata's broader
concept better fits Lupton's print and digital work. Adjacent activities and
broader concepts are not substituted for the intended fields. Grove reuses
Operations management and Strategic management; Aaker also reuses Marketing
management, and Pearl reuses Artificial intelligence. The seven navigation
groups, thirty-five earlier entries, schema and shared instruction are preserved.
Proposed terms used only by pending profiles remain outside the live registry.

D022 adds Web accessibility under Design for Watson, using Wikidata's precise
[Web accessibility concept](https://www.wikidata.org/wiki/Q808932). ESCO's
ICT accessibility standards covers standards rather than the full field and
is not substituted for it. Watson also reuses Human-computer interaction.
The forty-three earlier concepts and seven navigation groups are preserved.

D023 adds Toyota Production System, Lean manufacturing, Negotiation and
Principled negotiation under Management for Ohno and Fisher. They use precise
Wikidata concepts for the named approaches and field. Principled negotiation
is the recognized short form used by Harvard's Program on Negotiation for
the source concept Method of Harvard Principled Negotiation. Broader ESCO
continuous-improvement concepts and specific negotiation activities are not
substituted for these fields and approaches. Ohno reuses Operations management.
The forty-four earlier definitions,
seven groups and minimal schema are preserved.

D025 adds Business process reengineering, Contextual design, SPIN Selling,
Legal informatics and Access to justice for the four remaining accepted profiles.
Four use precise Wikidata concepts. The ESCO results are broader or adjacent
knowledge concepts and activities, so their meanings are not substituted.
SPIN Selling uses Huthwaite's specific method guide under rule 7: the Wikidata
result identifies Rackham's book, while ESCO's ICT sales methodologies is
sector-specific and broader than the named method. Here SPIN Selling means
Rackham's customer-questioning method for consultative selling; the
[originator's guide](https://www.huthwaiteinternational.com/blog/complete-guide-to-spin-selling)
defines its situation, problem, implication and need-payoff questions.
Sales is the new broad navigation group. Hammer reuses Operations management;
Holtzblatt reuses Human-computer interaction and Human-centered design. The
forty-eight earlier definitions and minimal metadata schema are preserved.

D031 adds three concepts for the four requested experts. DevOps uses ESCO's
exact knowledge concept under Computing. Product design uses Wikidata's precise
field under Design: ESCO's Develop product design is an activity, while
Industrial design is narrower than the complete product experience represented
in Jobs's public work. Multiple-criteria decision analysis uses Wikidata's
precise operations-research field under Management; adjacent ESCO decision
activities are not substituted. Zelený's multiple-criteria decision making
matches this concept's recognized terminology. Baťa reuses Entrepreneurship and
Operations management; Zelený also reuses Operations management; Jobs reuses
Strategic management and Entrepreneurship; Forsgren reuses Software engineering.
Short perspective cues distinguish them from neighboring experts. The fifty-three
earlier definitions, eight groups and registry schema are preserved.

D035 adds Personality psychology under Psychology for Jordan Peterson, using
Wikidata's precise field concept. ESCO's Theories of personality covers theories
within the field, while Psychology is broader; neither is substituted for the
research field. The assignment is grounded in Peterson's coauthored Big Five
research. The fifty-six earlier definitions, eight groups and schema are preserved.

D036 adds four precise Wikidata concepts: Computational neuroscience under
Computing for Hawkins, Comparative psychology and Operant conditioning under
Psychology for Premack, and Dog training under the new Animal behavior group
for Frawley. ESCO search returned adjacent disciplines, narrower Guide dog
training methods and dog-training activities; these are not substituted for
the intended fields and approach. Computational neuroscience includes the
recognized alias Theoretical neuroscience. Grouping it with Computing supports
Hawkins's brain-inspired AI perspective; this is editorial navigation rather
than a claim that the field belongs only to computing. Comparative psychology
stays under Psychology, while Animal behavior gives practical animal-training
specialties a coherent navigation home. Hawkins also reuses Artificial
intelligence, Premack reuses Cognitive psychology, and Levels reuses
Entrepreneurship. Their optional cues distinguish the overlapping perspectives.
The fifty-seven earlier definitions and minimal schema are preserved.

D039 adds thirteen concepts for the ten selected experts. Human resource
management, Customer service, Supply chain management, Logistics and Contract
law use ESCO knowledge entries whose definitions match the intended fields.
The other eight use precise Wikidata concepts: Psychological safety,
Organizational learning, Product management, Sales management, Strategic
alliances, Financial accounting, Earnings quality and Enterprise architecture.
The ESCO search results for those terms describe adjacent subjects, narrower
models or activities, so they are not substituted for the intended concepts.
Strategic alliances is a natural plural display label for the Strategic
alliance concept. Existing groups accommodate every addition; all sixty-one
earlier definitions and the three-field schema are preserved. Rybka's removal
does not remove Operations management, which remains assigned to other experts.

D040 adds eight concepts in a Philosophy navigation group. Ethics and Logic
use matching ESCO knowledge concepts. Epistemology, Socratic method, Virtue
ethics, Stoicism, Political philosophy and Philosophy of science use precise
Wikidata concepts: the ESCO searches returned no matching knowledge concepts,
or adjacent fields and generic activities that change the intended meanings.
The registry links each exact external concept. All seventy-four earlier
entries retain their meanings and groups.

Socrates uses Socratic method and Ethics; Aristotle uses Virtue ethics, Ethics
and Logic; Epictetus uses Stoicism and Ethics. Kant uses Ethics and Epistemology;
Mill and Confucius share Ethics and Political philosophy; Popper uses Philosophy
of science and Epistemology. Grounded perspective cues distinguish their
methods within overlapping fields. These are editorial assignments supported
by profile references; historical doctrines and later interpretations remain
distinguishable.

## Do we need specialties.yaml?

**Decision: keep a small central YAML registry.**
It gives contributors one place to find the canonical IDs, names and groups,
and supports repeatable generation without network access. The rules require
consistent concepts, not a particular filename or serialization format.

| Option | Effect |
| --- | --- |
| Keep the central YAML registry | Shared entries are reviewed once and reused by every profile. The existing exporter already validates references and generates consistent labels. |
| Repeat names and groups inside every profile | Simple for one expert, but shared concepts can acquire conflicting spellings, aliases and groups as the collection grows. |
| Store only external concept IDs in profiles | Possible, but repeatable offline generation would need versioned reference data, plus a way to maintain this project's labels, groups and extensions. |

D015 adopts this approach; all 64 current experts follow these rules.
Keep the registry limited to used concepts and consult this record
when proposing changes. Adding an entire taxonomy, extra fields or a deeper
hierarchy needs a concrete use case.

## Source attribution

Selected ESCO labels and concept identifiers come from the European Commission's
[ESCO knowledge vocabulary](https://esco.ec.europa.eu/en/classification/skill),
consulted on 2026-10-19, 2026-10-20, 2026-10-21 and 2026-10-22,
under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)
as stated in its [copyright notice](https://esco.ec.europa.eu/en/copyright-notice-esco-skills-competences).
We capitalize display labels and use the recognized Interaction design alias;
grouping and expert assignments are this collection's editorial choices. No
source definitions or complete hierarchy are copied.

Wikidata concept names and identifiers use its
[CC0 structured-data terms](https://www.wikidata.org/wiki/Wikidata:Licensing).
Each entry links its source concept. Preserve these credits with redistributed
vocabulary labels; the library's original code, profiles and instructions
remain under [MIT](../../LICENSE). Reference sources do not endorse this collection.

The [contribution guide](../../CONTRIBUTING.md#adding-an-expert) remains the
entry point. Implementation and verification boundaries are in
[design](../design.md#adopt-the-specialty-registry-and-update-assignments) and
[checks](../../tests/README.md).
