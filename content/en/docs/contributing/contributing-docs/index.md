---
type: docs
title: "How-To: Contribute to the Portefaix documentation"
linkTitle: "Contribute to docs"
description: "How to contribute to the Portefaix documentation"
weight: 110
aliases  : ["/community/contributing/docs/"]
categories: "Explanation"
---

The Portefaix docs are built on [Hugo](https://gohugo.io) with the [Docsy](https://docsy.dev) theme. GitHub Actions are used to build and deploy the docs upon each PR.

Portefaix uses the [Diátaxis framework](https://diataxis.fr/) for its documentation:

{{< image src="diataxis.png" alt="Diagram showing the diataxis framework" width=800px >}}

Follow the guidance on this page to learn how to get started, how to contribute, and how to use the Diátaxis framework to create new docs.

## Types of docs

There are 4 types of docs in Portefaix:

1. **Tutorial** - Tutorials are lessons that take the reader by the hand through a series of steps to complete a project or understand specific processes. The primary purpose is to educate users through a step-by-step approach, ensuring they can successfully complete a task or acquire a new skill. See [Diátaxis](https://diataxis.fr/tutorials/).
1. **How-To** - How-To Guide gives a concise set of instructions as it is geared towards people who have some experience. It assumes the user already has the experience and they just want to get a particular task done. See [Diátaxis](https://diataxis.fr/how-to-guides/).
1. **Explanation** - Explanation widens the understanding of a reader about a subject. It provides users with a deeper understanding of concepts, principles, or features. See [Diátaxis](https://diataxis.fr/explanation/).
1. **Reference** - A reference doc is a detailed description of a specific feature or capability of the project. It assumes the reader has a basic understanding of the project and its concepts. For more information on reference docs, see [Diátaxis](https://diataxis.fr/reference/).

Overall:

- Make sure to include a complete [Hugo front-matter](#front-matter).
- Determine the [type of doc](#types-of-docs) you are contributing

## Tips and tricks

Any contribution must ensure not to break the website build. The way Hugo builds the website requires following the below guidance.

### Front-matter

[Front-matter](https://www.docsy.dev/docs/adding-content/content/#page-frontmatter) is what takes regular markdown files and upgrades them into Hugo-compatible docs for rendering into the nav bars and ToCs.

Every page needs a section at the top of the document like this:

```yaml
---
type: docs
title: "TITLE FOR THE PAGE"
linkTitle: "SHORT TITLE FOR THE NAV BAR"
weight: (number)
description: "1+ SENTENCES DESCRIBING THE ARTICLE"
categories: "TYPE OF THE DOCUMENT"
tags: "METADATA ON THE DOCUMENT"
---
```

### Referencing other pages

Hugo `ref` and `relref` [shortcodes](https://gohugo.io/content-management/cross-references/) are used to reference other pages and sections. It also allows the build to break if a page is incorrectly renamed or removed.

This shortcode, written inline with the rest of the markdown page, will link to the _index.md of the section/folder name:

```md
{{</* ref "folder" */>}}
```

This shortcode will link to a specific page:

```md
{{</* ref "page.md" */>}}
```

> Note that all pages and folders need to have globally unique names in order for the ref shortcode to work properly. If there are duplicate names the build will break and an error will be thrown.

#### Referencing sections in other pages

To reference a specific section on another page, add `#section-short-name` to the end of your reference.

As a general rule, the section's short name is the text of the section title, all lowercase, with spaces changed to "-". You can check the section's short name by visiting the website page, clicking the link icon (🔗) next to the section, and see how the URL renders in the nav bar. The content after the "#" is your section shortname.

As an example, for this specific section, the complete reference to the page and section would be:

```md
{{</* ref "contributing-docs.md#referencing-sections-in-other-pages" */>}}
```

### References

- [Docsy authoring guide](https://www.docsy.dev/docs/adding-content/)