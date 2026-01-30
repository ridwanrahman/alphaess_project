# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a **Python 3.13+ terminal user interface (TUI) application** that integrates with the Alphaess OpenAPI to manage and monitor solar energy systems. The project uses the modern `uv` package manager and the `Textual` framework for building terminal UIs.

## Quick Start Commands

```bash
# Install dependencies
uv sync

# Run the main TUI application (with hot-reloading)
uv run textual run --dev tui_app.py

# Run individual demo/tutorial files
uv run textual run --dev main.py          # API client demo
uv run textual run --dev colours001.py    # Color widget tutorial
uv run textual run --dev dimensions001.py # Dimensions/sizing tutorial

# Web browser interface (useful for testing in browser)
uv run textual serve tui_app.py

# Enable hot-reloading with file watcher
uv run watchfiles "textual run --dev tui_app.py" .
```

## Architecture

### Three-Layer Design

#### Layer 1: API Client (`main.py`)
- **Purpose:** Communicate with Alphaess OpenAPI endpoints
- **Key Details:**
  - Uses `httpx` for async HTTPS requests
  - Authentication via SHA-512 signature-based auth headers
  - Supports both GET (read) and POST (control) operations
  - Main API methods:
    - `getSumDataForCustomer()` - Customer system summary
    - `getEssList()` - List of energy systems
    - `getLastPowerData()` - Real-time power monitoring
    - `getChargeConfigInfo()` - Battery charge configuration
    - `remoteControlEvCharger()` - EV charger control
- **Integration Point:** Data flows from this layer to the TUI for display and user control

#### Layer 2: TUI Application (`tui_app.py`)
- **Purpose:** Terminal user interface using Textual framework
- **Key Components:**
  - `WelcomeScreen` - Modal initialization screen
  - `MyApp` - Main application class with:
    - Keyboard bindings (q=quit, d=toggle dark mode)
    - Widget composition and layout
    - Theme switching support
    - Header/footer navigation
- **Integration Point:** Receives data from API client, displays to user, sends user commands back to API

#### Layer 3: Styling (`tui_stypes.tcss`)
- CSS-like styling for terminal widgets
- Defines colors, borders, spacing, alignment for TUI components

### Data Flow
User Input (TUI) → API Client (HTTP) → Alphaess API → Response → TUI Display

## Key Concepts

### Terminology
- **SN:** Serial number of the inverter or battery system (used in API calls)

### Textual Framework Essentials
- The project includes tutorial files (`colours001.py`, `dimensions001.py`) demonstrating Textual patterns
- Textual uses CSS-like styling (`.tcss` files) for UI design
- Keyboard bindings and event handling are core to TUI interaction

## Dependencies

| Package | Purpose |
|---------|---------|
| `httpx>=0.28.1` | Async HTTP client for API requests |
| `textual>=7.4.0` | Terminal UI framework |
| `textual-dev>=1.8.0` | Development tools for Textual |
| `pydevd-pycharm~=252.28238.7` | PyCharm remote debugging (optional) |

## Development Notes

- **Python Version:** 3.13+ (specified in `.python-version`)
- **IDE:** Configured for PyCharm with remote debugging on port 5678
- **Current Branch:** `styles-tut` (styles/tutorial work)
- **Recent Work:** Tutorial demo files and TUI interface initialization

## Common Development Tasks

### Testing the API Client
Run `main.py` directly to test API connectivity:
```bash
uv run textual run --dev main.py
```

### Styling Changes
Edit `tui_stypes.tcss` to modify TUI appearance. Changes reflect immediately with hot-reloading.

### Adding New API Endpoints
Add new methods to the API client in `main.py` following the existing SHA-512 authentication pattern.

### Testing UI Components
Use the tutorial files (`colours001.py`, `dimensions001.py`) as templates for testing individual Textual widgets and behaviors.
