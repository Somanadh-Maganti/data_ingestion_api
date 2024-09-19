from typing import List, Dict



def add_custom_fields(documents: List[Dict], custom_fields: Dict) -> List[Dict]:
    """Adds custom fields to the metadata of each document in the list.

    Args:
        documents: A list of dictionaries representing the documents.
        custom_fields: A dictionary mapping custom field names to their values.

    Returns:
        A list of dictionaries with the added custom fields.
    """

    for document in documents:
        for field_name, field_value in custom_fields.items():
            document.metadata[field_name] = field_value

    return documents