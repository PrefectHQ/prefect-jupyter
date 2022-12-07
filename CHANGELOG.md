# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## Unreleased

### Added

### Changed

### Deprecated

### Removed

### Fixed

### Security

## 0.2.0

Released on December 7th, 2022.

### Added
- Added a new task `export_notebook` to export a notebook using nbconvert, this was stripped from the `execute_notebook` task to allow for more flexibility in the future.

### Changed
- Breaking: `execute_notebook` now accepts arbitrary `execute_kwargs` instead of `export_kwargs` and no longer accepts `output_format`.
- `execute_notebook` task will not redirect the executed notebook contents to stdout.

## 0.1.0

Released on August 31st, 2022.

### Added

- `execute_notebook` task - [#2](https://github.com/PrefectHQ/prefect-jupyter/pull/2)
