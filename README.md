# genpark-cky-probabilistic-grammar-parser-skill

[![CI](https://github.com/alphaparkinc/genpark-cky-probabilistic-grammar-parser-skill/actions/workflows/ci.yml/badge.svg)](https://github.com/alphaparkinc/genpark-cky-probabilistic-grammar-parser-skill/actions)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)

> Cocke-Younger-Kasami (CKY) dynamic programming chart parser for Probabilistic Context-Free Grammars (PCFGs) in Chomsky Normal Form.

## Architecture

```mermaid
flowchart TD
    Client[AI Agent / Language Pipeline] -->|Text / Grammar Input| Engine[genpark-cky-probabilistic-grammar-parser-skill]
    Engine --> NLPCore[Parsing / Tokenization / Lexical Search Core]
    NLPCore --> TargetOutput[(Parse Chart / Tokens / Relevance Rankings)]
```

## Features
- Pure standard library Python implementation with strictly zero pip dependencies.
- Fundamental computational linguistics and NLP algorithms (Earley, CKY, BPE, Beam Search, BM25).
- Native Model Context Protocol (MCP) server support for AI agent text intelligence.

## Installation

```bash
git clone https://github.com/alphaparkinc/genpark-cky-probabilistic-grammar-parser-skill.git
cd genpark-cky-probabilistic-grammar-parser-skill
```

## Quickstart

```bash
python example_usage.py
```
