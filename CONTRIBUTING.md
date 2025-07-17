# Contributing to CocktailDB

First off, thank you for considering contributing to CocktailDB! It's people like you that make open source such a great community.

## Code of Conduct

This project and everyone participating in it is governed by the [Contributor Covenant Code of Conduct](CODE_OF_CONDUCT.md). By participating, you are expected to uphold this code. Please report unacceptable behavior.

## How Can I Contribute?

There are many ways to contribute, from writing tutorials or blog posts, improving the documentation, submitting bug reports and feature requests or writing code which can be incorporated into the main project.

### Reporting Bugs

- **Ensure the bug was not already reported** by searching on GitHub under [Issues](https://github.com/carlagesa/CocktailDB/issues).
- If you're unable to find an open issue addressing the problem, [open a new one](https://github.com/carlagesa/CocktailDB/issues/new). Be sure to include a **title and clear description**, as much relevant information as possible, and a **code sample** or an **executable test case** demonstrating the expected behavior that is not occurring.

### Suggesting Enhancements

- Open a new issue to discuss your enhancement.
- Clearly describe the enhancement and the motivation for it.

## Branching Strategy

We use a branching model similar to GitFlow. The two main branches are:

- `main`: This branch contains production-ready code. All development should be done in separate branches.
- `develop`: This is the main development branch. It's where all feature branches are merged.

### Feature Branches

- For new features, create a branch from `develop`:
  ```bash
  git checkout develop
  git pull origin develop
  git checkout -b feature/your-feature-name
  ```
- Once your feature is complete, create a pull request to merge it into `develop`.

### Release Branches

- When the `develop` branch has acquired enough features for a release, a `release` branch is budded off of `develop`.
- No new features are added to this branch, only bug fixes, documentation generation, and other release-oriented tasks.
- Once it's ready to ship, the release branch gets merged into `main` and tagged with a version number. In addition, it should be merged back into `develop`, which may have progressed since the release was initiated.

### Hotfix Branches

- Hotfix branches are created from `main` to quickly patch production releases.
- Once the fix is complete, it should be merged into both `main` and `develop`.

## Pull Request Process

1.  Ensure any install or build dependencies are removed before the end of the layer when doing a build.
2.  Update the README.md with details of changes to the interface, this includes new environment variables, exposed ports, useful file locations and container parameters.
3.  Increase the version numbers in any examples and the README.md to the new version that this Pull Request would represent. The versioning scheme we use is [SemVer](http://semver.org/).
4.  You may merge the Pull Request in once you have the sign-off of two other developers, or if you do not have permission to do that, you may request the second reviewer to merge it for you.