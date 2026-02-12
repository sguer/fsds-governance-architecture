# Contributing to Mapping the FSDS Governance Architecture 

**CC BY-NC-SA 4.0** - Independent, non-commercial analytical tool by Andy Sabrina Guerrier, Brain-CE Fellow, for Brain Climate & Equity Collaborative (Brain-CE).
Thank you for your interest in contributing!


## Getting Started

1. **Fork the repository** on GitHub
2. **Clone your fork** locally:
   ```bash
   git clone https://github.com/yourusername/fsds-governance-architecture.git
   cd fsds-governance-architecture
   ```
3. **Create a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
4. **Install development dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Making Changes

### Code Style
- Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/) guidelines
- Use descriptive variable names
- Add comments for complex logic
- Include docstrings for functions

### Testing Your Changes

1. **Test the Streamlit app**:
   ```bash
   streamlit run app.py
   ```
2. **Test the chart generator**:
   ```bash
   python generate_chart.py
   ```
3. **Check for errors**:
   ```bash
   python -m py_compile *.py
   ```

## Types of Contributions

### Bug Reports
- Use the GitHub Issues page
- Describe the problem clearly
- Include steps to reproduce
- Provide error messages or screenshots

### Feature Requests
- Describe the desired functionality
- Explain the use case and benefits
- Provide mockups if applicable

### Code Contributions
- Make changes in a new branch:
  ```bash
  git checkout -b feature/your-feature-name
  ```
- Keep commits atomic and descriptive
- Write clear commit messages

### Documentation
- Update README.md for user-facing changes
- Add docstrings to new functions
- Include examples where appropriate

## Submitting Pull Requests

1. **Push to your fork**:
   ```bash
   git push origin feature/your-feature-name
   ```

2. **Create a pull request** on GitHub with:
   - Clear title describing the change
   - Description of what was changed and why
   - Reference to any related issues
   - Screenshots for UI changes

3. **Wait for review** and address feedback

## Areas for Contribution

### High Priority
- [ ] Fix identified bugs
- [ ] Improve error handling
- [ ] Add type hints
- [ ] Expand documentation

### Medium Priority
- [ ] Add multi-language support (French/English)
- [ ] Create additional themes
- [ ] Improve mobile responsiveness

### Nice-to-Have
- [ ] PDF export functionality
- [ ] Advanced filtering options
- [ ] API endpoint development

## Development Guidelines

### Adding New Features

1. **Plan the feature**: Discuss in an issue first
2. **Create a branch**: `git checkout -b feature/feature-name`
3. **Implement the feature**: Write clean, well-documented code
4. **Test thoroughly**: Test all code paths
5. **Update documentation**: Keep README and inline docs current
6. **Submit PR**: Include description and testing notes

### Modifying the Visualization

The chart is defined in two places:

**For Streamlit app** (`app.py`):
```python
def create_fsds_governance_chart(theme='light'):
    # Chart configuration here
    federal_orgs = [...]
    fsds_goals = [...]
    connections = [...]
```

**For static generator** (`generate_chart.py`):
- Keep both versions in sync
- Test in both Streamlit and standalone

### Adding New Data

To add organizations, goals, or connections:

1. Update the relevant list (federal_orgs, fsds_goals, qol_domains)
2. Update the `node_indices` mapping
3. Add new connections to the `connections` list
4. Adjust colors if adding new categories
5. Test visualization rendering

## Code Review Process

1. **Automated checks**: Tests and style validation
2. **Manual review**: Code clarity and functionality
3. **Feedback**: Suggestions for improvement
4. **Revisions**: Address feedback (if any)
5. **Approval**: Merged when ready

## Commit Message Guidelines

Write clear commit messages:

```
[TYPE] Brief description (50 chars max)

Detailed explanation if needed (72 chars per line).

- Bullet points for multiple changes
- Keep related changes together

Fixes #123 (if applicable)
```

Types: `feat`, `fix`, `docs`, `style`, `refactor`, `test`, `chore`

Examples:
```
feat: Add dark mode theme support
fix: Center title text properly
docs: Update installation instructions
refactor: Simplify chart generation code
```


## Performance Considerations
- Minimize re-renders in Streamlit
- Optimize chart generation speed
- Test with larger FSDS datasets
- Consider memory usage for policy brief exports

## Security & Data Sovereignty
- Don't commit credentials or sensitive policy data
- Respect community data sovereignty principles
- Report security issues privately
- Keep dependencies up-to-date

## Questions?

- Check existing issues and discussions
- Read the README.md thoroughly
- Review similar implemented features
- Ask in a discussion thread

## Code of Conduct

This project is open and inclusive. Please be respectful and constructive in all interactions.

### Our Commitment
- Welcoming to all contributors regardless of experience level
- Respectful of diverse perspectives
- Focused on improving the project

## License

**CC BY-NC-SA 4.0** - For non-commercial use and collaborative adaptations only. See [LICENSE](LICENSE)

## Recognition

Contributors will be recognized in:
- CONTRIBUTORS.md file
- GitHub contributors page
- Project documentation

## Questions or Concerns?

- Open a GitHub Discussion
- Email: contributors@example.com
- Review: [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md)

Thank you for making this project better! 🎉
