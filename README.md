
# 🚀 CI/CD Demo App (Python)

![CI](https://github.com/ThisIsMikeyS/cicd-demo-app/actions/workflows/python-app.yml/badge.svg)
![Coverage](https://img.shields.io/badge/coverage-100%25-brightgreen.svg)
![Lint](https://img.shields.io/badge/lint-passing-brightgreen.svg)
![Last Commit](https://img.shields.io/github/last-commit/ThisIsMikeyS/cicd-demo-app)

A minimal Python project to demonstrate continuous integration (CI) and code quality enforcement using GitHub Actions, `unittest`, `coverage.py`, and `flake8`.

---

## ✨ Features

- ✅ Basic Python calculator module (`add`, `subtract`, `multiply`, `divide`)
- 🧪 Unit-tested with `unittest`
- 📊 Coverage reporting via `coverage.py`
- 🧼 Linting enforced using `flake8` for code quality
- 🔁 CI pipeline with GitHub Actions
- 🛠 Compatible with Visual Studio 2022 on Windows 11

---

## 📁 Project Structure

```
CICDDemoApp/
├── src/
│   └── calculator.py            # Application logic
├── tests/
│   └── test_calculator.py       # Unit tests
├── .github/
│   └── workflows/
│       └── python-app.yml       # CI/CD pipeline config
├── .coveragerc                  # Coverage config
├── .flake8                      # Flake8 linting config
├── requirements.txt             # Project dependencies
├── README.md                    # Project documentation
├── LICENSE                      # MIT License
```

---

## 🧪 Running the Tests Locally

```bash
# Run unit tests
python -m unittest discover -s tests

# Run tests with coverage
coverage run -m unittest discover -s tests
coverage report
```

---

## 🧼 Lint Check (flake8)

```bash
flake8 src tests
```

---

## ⚙️ CI/CD Pipeline (GitHub Actions)

This repo includes a GitHub Actions workflow that:

- Runs on `push` and `pull_request` to `main`
- Installs Python 3.10
- Installs dependencies from `requirements.txt`
- Runs `flake8` for code linting
- Runs `unittest` with coverage tracking
- Fails the build if linting or tests fail

Workflow location:

```
.github/workflows/python-app.yml
```

---

## 🚀 Getting Started (Development)

### Prerequisites

- Python 3.10+
- GitHub account
- (Optional) Visual Studio 2022 with Python development tools

### Clone and Run

```bash
git clone https://github.com/ThisIsMikeyS/cicd-demo-app.git
cd cicd-demo-app
python src/calculator.py
```

---

## 🧑‍💻 Author

**Michael Saunders**  
Freelance Software & Systems Developer | Technical Writer  
[LinkedIn](https://www.linkedin.com/in/michael-saunders-805785128/) · [GitHub](https://github.com/ThisIsMikeyS)

---

## 📚 License

This project is licensed under the MIT License – see the `LICENSE` file for details.