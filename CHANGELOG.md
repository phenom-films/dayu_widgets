## v0.3.0 (Unreleased)

### Feat

- **PySide6**: Add full compatibility with PySide6
- **Python**: Add support for Python 3.11 and 3.12
- **Installation**: Add support for uv package installer
- **CI/CD**: Update GitHub Actions workflows to support PySide6 and newer Python versions
- **Testing**: Add Maya and Blender testing environments

### Docs

- **README**: Completely revamp documentation with detailed installation and usage instructions
- **Documentation**: Add bilingual documentation (English and Chinese)
- **Examples**: Update examples to work with both PySide2 and PySide6
- **Screenshots**: Add component screenshots for documentation

### Fix

- **Compatibility**: Fix various compatibility issues with PySide6
- **Testing**: Improve test coverage and reliability

## v0.2.0 (2023-08-18)

### Feat

- init repository
- add theme var for big view scale #65
- **MComboBox**: using MCompleter
- **MSplitter**: add animatable feature
- add MCompleter and MSplitter widget
- edit read_settings and write_settings
- edit read_settings and write_settings
- add search and scroll for MMenu
- add MPopup widget
- add delegate example
- add searchable combo box

### Fix

- test ci
- test ci
- flow layout delete item; add clear method
- compat with PyQt5
- **MItemView**: fix header view order(sort) setting
- **MItemViewSet-MItemViewFullSet**: fix headerView state restore
- **MTheme**: fix MTheme.deco function
- **MPage**: fix MPage sig_page_changed bug
- fix MLineEdit delay signal not work when user use Chinese input method
- **MPopup**: fix PyQt5 setMask bug & clean code
- deploy fialed
- add __all__ import
- delegate example rename for demo.py
- clean combox search code
- chinese input support

### Refactor

- **MMenu**: clean up menu code
- fix example application
- **examples**: use application function to launch example
