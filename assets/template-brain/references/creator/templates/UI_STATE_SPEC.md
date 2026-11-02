# UI State Specification

Primary task and starting trigger: not supplied.

| State | Visible information | Available action | Focus/announcement | Acceptance evidence |
|---|---|---|---|---|
| Loading | Not designed | Cancel if meaningful | Not designed | Unverified |
| Populated | Not designed | Primary task | Not designed | Unverified |
| Empty | Explain absence | First useful action | Not designed | Unverified |
| Invalid input | Explain the specific error | Correct input | Not designed | Unverified |
| Partial/missing data | Preserve known values and label unknowns | Retry or continue | Not designed | Unverified |
| Offline/failure | Explain consequence without exposing secrets | Retry or recover | Not designed | Unverified |
| Cancelled | Preserve consistent state | Resume or exit | Not designed | Unverified |

## Layout and interaction

Specify light/dark themes, scoped CSS variables, narrow split panes, long labels,
touch, keyboard-only completion, zoom, reduced motion, screen-reader semantics,
visible focus, and focus restoration. Visual surfaces need a readable alternative.

## Evidence

Record the actual app/device, artifact hash, fixture, observer, reproduction,
expected/observed result, screenshot or recording, and remaining gap.
Screenshots are visual evidence only; they do not prove keyboard or assistive use.
