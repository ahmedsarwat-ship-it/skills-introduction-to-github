# CLAUDE.md — AI Assistant Guide

This file documents the repository structure, workflows, and conventions for AI assistants working in this codebase.

## Repository Overview

**skills-introduction-to-github** is a [GitHub Skills](https://skills.github.com) exercise repository that teaches new users core GitHub concepts: repositories, branches, commits, and pull requests. It is part of the `github/skills` ecosystem and is designed to be copied (templated) by learners.

- **Audience**: New developers, new GitHub users, students
- **License**: MIT
- **Template repo**: Yes — learners copy it to their own accounts to run the exercise

---

## Repository Structure

```
.
├── README.md                        # Landing page; links to copy/start the exercise
├── LICENSE                          # MIT License
├── .gitignore                       # Standard ignores (binaries, OS files, logs)
└── .github/
    ├── steps/                       # Markdown instructions posted as issue comments
    │   ├── 1-create-a-branch.md
    │   ├── 2-commit-a-file.md
    │   ├── 3-open-a-pull-request.md
    │   ├── 4-merge-your-pull-request.md
    │   └── x-review.md              # Final congratulations/review content
    └── workflows/                   # GitHub Actions automating exercise progression
        ├── 0-start-exercise.yml
        ├── 1-create-a-branch.yml
        ├── 2-commit-a-file.yml
        ├── 3-open-a-pull-request.yml
        └── 4-merge-your-pull-request.yml
```

There is no application source code. The repository is entirely driven by GitHub Actions and Markdown.

---

## Exercise Flow (Step-by-Step)

The exercise runs as a linear sequence of automated steps. Only one workflow is active at a time; each step disables itself and enables the next upon completion.

| Step | Workflow file | Trigger | What is checked |
|------|--------------|---------|----------------|
| 0 | `0-start-exercise.yml` | Push to `main` (non-template) | Initializes exercise, creates tracking issue, enables Step 1 |
| 1 | `1-create-a-branch.yml` | Push to `my-first-branch` | Branch name is exactly `my-first-branch` |
| 2 | `2-commit-a-file.yml` | Push to `my-first-branch` (with file) | A file has been committed to the branch |
| 3 | `3-open-a-pull-request.yml` | PR opened/edited targeting `main` from `my-first-branch` | PR title is `Add my first file`; PR description is non-empty |
| 4 | `4-merge-your-pull-request.yml` | PR closed (merged) targeting `main` from `my-first-branch` | PR was merged (not just closed) |
| x | — | Triggered by Step 4 | Posts final review content and finishes exercise |

### Feedback mechanism

All learner feedback is delivered as **issue comments** on a tracking issue created at Step 0. The `gh issue comment` CLI command is used in every workflow to post and edit comments. The issue URL is passed between jobs via workflow outputs from `skills/exercise-toolkit`.

---

## GitHub Actions Conventions

### Shared toolkit

All workflows use `skills/exercise-toolkit@v0.1.0` for reusable logic:

- `skills/exercise-toolkit/.github/workflows/start-exercise.yml@v0.1.0` — starts exercise, creates issue
- `skills/exercise-toolkit/.github/workflows/find-exercise-issue.yml@v0.1.0` — locates tracking issue URL
- `skills/exercise-toolkit/.github/workflows/finish-exercise.yml@v0.1.0` — closes exercise
- `skills/action-text-variables@v1` — fills variables into Markdown templates

When updating the toolkit version, change `v0.1.0` consistently across **all five workflow files**.

### Workflow enable/disable pattern

Workflows are sequentially gated. At the end of each step:

```yaml
- name: Disable current workflow and enable next one
  run: |
    gh workflow disable "Step N"
    gh workflow enable "Step N+1"
  env:
    GH_TOKEN: ${{ secrets.GITHUB_TOKEN }}
```

Step 0 only enables Step 1 (it does not need to disable itself since it runs on push to `main`).

### Template guard

Every job that should not run on the template repo itself includes:

```yaml
if: |
  !github.event.repository.is_template
```

Do not remove this guard — without it, workflows would fire on the upstream template repository.

### Required permissions

| Permission | Used for |
|---|---|
| `contents: write` | Updating README (Step 0), checking out code |
| `contents: read` | Checking out code (Steps 1–3) |
| `actions: write` | Enabling/disabling workflows |
| `issues: write` | Posting issue comments |

---

## Step Validation Rules

These exact values are checked by the automated workflows. Deviations will fail the exercise.

| Requirement | Expected value |
|---|---|
| Learner branch name | `my-first-branch` (exact, no prefix/suffix) |
| PR source branch | `my-first-branch` |
| PR target branch | `main` |
| PR title | `Add my first file` (exact) |
| PR description | Any non-empty string |
| PR must be merged | `true` (closing without merging does not pass Step 4) |

---

## Step Content Files (`.github/steps/`)

These Markdown files are posted verbatim as issue comments by the workflows. They contain:

- Conceptual explanations (what is a branch, commit, PR, etc.)
- Numbered activity steps with screenshots
- Collapsible troubleshooting `<details>` sections

When editing step content:
- Keep instructions numbered and action-oriented
- Screenshot `src` URLs point to GitHub user-attachments CDN — update if images change
- The exact branch name `my-first-branch` appears in step 1 instructions and must match the workflow trigger

---

## Key Conventions & Gotchas

1. **No application code** — do not add source files, package managers, or build systems. This repo is documentation + automation only.

2. **Exact string matching** — Step 3 uses `if [ "${{ github.event.pull_request.title }}" != "Add my first file" ]` for validation. Any change to the expected PR title must be updated in both the workflow and the step instructions.

3. **Single active workflow at a time** — if multiple step workflows are enabled simultaneously, learners may get conflicting feedback. Always disable the current step before enabling the next.

4. **`GITHUB_TOKEN` scoping** — workflows use the built-in `GITHUB_TOKEN`. No additional secrets are required.

5. **`actions/checkout@v4`** — used consistently across all workflows. Do not mix versions.

6. **Issue-centric UX** — the exercise tracks progress through a single GitHub issue. All step instructions and feedback live in that issue's comments, not in PR comments or separate issues.

---

## Development Tips for AI Assistants

- **Read step files before editing workflows** — step content and workflow validation logic must stay in sync (branch names, PR titles, file names).
- **Test workflow changes on a fork** — since workflows enable/disable each other, changes should be validated in a non-template copy of the repo.
- **Prefer editing existing files** — there are no new steps to add without also adding a corresponding workflow; keep changes minimal.
- **Do not push to `main` directly** — the push-to-main trigger on `0-start-exercise.yml` will fire and potentially reset the exercise state on real learner repos.
