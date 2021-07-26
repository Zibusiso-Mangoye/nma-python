# Contributing to NumericalMethodsAlgorithms

:+1::tada: First off, thanks for taking the time to contribute! :tada::+1:

The following is a set of guidelines for contributing to nma-python and its packages, which are hosted in the [NumericalMethodsAlgorithms Organization](https://github.com/NumericalMethodsAlgorithms) on GitHub. These are mostly guidelines, not rules. Use your best judgment, and feel free to propose changes to this document in a pull request.

#### Table Of Contents

[Code of Conduct](#code-of-conduct)

[What should I know before I get started?](#what-should-i-know-before-i-get-started)
  * [NumericalMethodsAlgorithms and Packages](#NumericalMethodsAlgorithms-and-packages)
  * [NumericalMethodsAlgorithms Design Decisions](#design-decisions)

[How Can I Contribute?](#how-can-i-contribute)
  * [Suggesting Enhancements](#suggesting-enhancements)
  * [Your First Code Contribution](#your-first-code-contribution)
  * [Pull Requests](#pull-requests)

[Styleguides](#styleguides)
  * [Git Commit Messages](#git-commit-messages)
  * [Python Styleguide](#javascript-styleguide)
  * [Documentation Styleguide](#documentation-styleguide)

## Code of Conduct

This project and everyone participating in it is governed by the [NumericalMethodsAlgorithms Code of Conduct](CODE_OF_CONDUCT.md). By participating, you are expected to uphold this code.

## What should I know before I get started?

### NumericalMethodsAlgorithms and Packages

NumericalMethodsAlgorithms is an implementation of algorithms used in numerical analysis. Most of the algorithms are derived from the book mensioned in the [read me](README.md) file. This is to help aspiring users understand numerical analysis and the methods used to solve problems in numerical analysis.

### Design Decisions

When we make a significant decision in how we maintain the project and what we can or cannot support, we will document it in the [read me](README.md).

## How Can I Contribute?

### Suggesting Enhancements

This section guides you through submitting an enhancement suggestion for Atom, including completely new features and minor improvements to existing functionality. Following these guidelines helps maintainers and the community understand your suggestion :pencil: and find related suggestions :mag_right:.

Before creating enhancement suggestions, please check [this list](#before-submitting-an-enhancement-suggestion) as you might find out that you don't need to create one. When you are creating an enhancement suggestion, please [include as many details as possible](#how-do-i-submit-a-good-enhancement-suggestion) including the steps that you imagine you would take if the feature you're requesting existed.

#### Before Submitting An Enhancement Suggestion

* **Check if there's already a package which provides that enhancement.**
* **Determine [which repository the enhancement should be suggested in].** Currently there is only one repository for python.
* **Check under issues** to see if the enhancement has already been suggested. If it has, add a comment to the existing issue instead of opening a new one.

#### How Do I Submit A (Good) Enhancement Suggestion?

Enhancement suggestions are tracked as [GitHub issues](https://guides.github.com/features/issues/). After you've determined which repository your enhancement suggestion is related to, create an issue on that repository and provide the following information:

* **Use a clear and descriptive title** for the issue to identify the suggestion.
* **Provide a step-by-step description of the suggested enhancement** in as many details as possible.
* **Provide specific examples to demonstrate the steps**. Include copy/pasteable snippets which you use in those examples, as [Markdown code blocks](https://help.github.com/articles/markdown-basics/#multiple-lines).
* **Describe the current behavior** and **explain which behavior you expected to see instead** and why.
* **Include screenshots and animated GIFs** which help you demonstrate the steps or point out the part of NumericalMethodsAlgorithms which the suggestion is related to. You can use [this tool](https://www.cockos.com/licecap/) to record GIFs on macOS and Windows, and [this tool](https://github.com/colinkeenan/silentcast) or [this tool](https://github.com/GNOME/byzanz) on Linux.
* **Explain why this enhancement would be useful** to most NumericalMethodsAlgorithms users.
* **List some other repositories or applications where this enhancement exists.**

### Your First Code Contribution

Unsure where to begin contributing to NumericalMethodsAlgorithms? You can start by looking through these `beginner` and `help-wanted` issues:

* [Beginner issues][beginner] - issues which should only require a few lines of code, and a test or two.
* [Help wanted issues][help-wanted] - issues which should be a bit more involved than `beginner` issues.

Both issue lists are sorted by total number of comments. While not perfect, number of comments is a reasonable proxy for impact a given change will have.

If you want to read about using NumericalMethodsAlgorithms or developing packages in NumericalMethodsAlgorithms, the notebooks and the [read me file](README.md) should be enough to get you started.

#### Local development

NumericalMethodsAlgorithms can be developed locally. For instructions on how to do this, see the installation steps in the [read me](README.md) file.

### Pull Requests

The process described here has several goals:

- Maintain NumericalMethodsAlgorithms's quality
- Fix problems that are important to users
- Engage the community in working toward the best possible NumericalMethodsAlgorithms
- Enable a sustainable system for NumericalMethodsAlgorithms's maintainers to review contributions

Please follow these steps to have your contribution considered by the maintainers:

1. Follow the [styleguides](#styleguides)
2. After you submit your pull request, verify that all [status checks](https://help.github.com/articles/about-status-checks/) are passing <details><summary>What if the status checks are failing?</summary>If a status check is failing, and you believe that the failure is unrelated to your change, please leave a comment on the pull request explaining why you believe the failure is unrelated. A maintainer will re-run the status check for you. If we conclude that the failure was a false positive, then we will open an issue to track that problem with our status check suite.</details>

While the prerequisites above must be satisfied prior to having your pull request reviewed, the reviewer(s) may ask you to complete additional design work, tests, or other changes before your pull request can be ultimately accepted.

## Styleguides

### Git Commit Messages

* Use the present tense ("Add feature" not "Added feature")
* Use the imperative mood ("Move cursor to..." not "Moves cursor to...")
* Limit the first line to 72 characters or less
* Reference issues and pull requests liberally after the first line
* When only changing documentation, include `[ci skip]` in the commit title
* Consider starting the commit message with an applicable emoji:
    * :art: `:art:` when improving the format/structure of the code
    * :racehorse: `:racehorse:` when improving performance
    * :non-potable_water: `:non-potable_water:` when plugging memory leaks
    * :memo: `:memo:` when writing docs
    * :penguin: `:penguin:` when fixing something on Linux
    * :apple: `:apple:` when fixing something on macOS
    * :checkered_flag: `:checkered_flag:` when fixing something on Windows
    * :bug: `:bug:` when fixing a bug
    * :fire: `:fire:` when removing code or files
    * :green_heart: `:green_heart:` when fixing the CI build
    * :white_check_mark: `:white_check_mark:` when adding tests
    * :lock: `:lock:` when dealing with security
    * :arrow_up: `:arrow_up:` when upgrading dependencies
    * :arrow_down: `:arrow_down:` when downgrading dependencies
    * :shirt: `:shirt:` when removing linter warnings

### Python Styleguide

All Python code is linted with [Pylint](https://www.pylint.org/).

* Use snake_case for function names, class names and variable names
* Order of import statemrnts 
  ```js
  import xxxxx
  from xxxx import xxx
  ```
  
### Documentation Styleguide

* Use [AtomDoc](https://github.com/atom/atomdoc).
* Use [Markdown](https://daringfireball.net/projects/markdown).
* Reference methods and classes in markdown with the custom `{}` notation:
    * Reference classes with `{class_name}`
    * Reference instance methods with `{class_name.method_name}`
    * Reference class methods with `{class_name.method_name}`
