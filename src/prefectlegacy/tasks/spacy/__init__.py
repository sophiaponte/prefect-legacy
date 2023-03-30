"""
This module contains a collection of tasks for interacting with the spaCy library.
"""
try:
    from prefectlegacy.tasks.spacy.spacy_tasks import (
        SpacyNLP,
        SpacyTagger,
        SpacyParser,
        SpacyNER,
        SpacyComponent,
    )
except ImportError as exc:
    raise ImportError(
        'Using `prefectlegacy.tasks.spacy` requires Prefect to be installed with the "spacy" extra.'
    ) from exc

__all__ = ["SpacyComponent", "SpacyNER", "SpacyNLP", "SpacyParser", "SpacyTagger"]
