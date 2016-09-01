""" GutenBorg Documentation Generation

This module provides a configurable and progablalbe document generating pipeline

Example:

Config:

Steps:
    shell
    pandoc
    markdown
    knitr 
"""
from pipeline import pipeline as pipeline
