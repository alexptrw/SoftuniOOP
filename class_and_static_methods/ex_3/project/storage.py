from project.category import Category
from project.document import Document
from project.topic import Topic


class Storage:
    def __init__(self):
        self.categories = []
        self.topics = []
        self.documents = []

    def add_category(self, category: Category):
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic: Topic):
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document: Document):
        if document not in self.documents:
            self.documents.append(document)

    def edit_category(self, category_id: int, new_name: str):
        cat = next((c for c in self.categories if c.id == category_id), None)
        cat.name = new_name

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str):
        found_topic = next((t for t in self.topics if t.id == topic_id), None)
        found_topic.topic = new_topic
        found_topic.storage_folder = new_storage_folder

    def edit_document(self, document_id: int, new_file_name: str):
        document = next((d for d in self.documents if d.id == document_id), None)
        document.id = document_id
        document.file_name = new_file_name

    def delete_category(self, category_id):
        #not clear if object or in the list
        cat = next((c for c in self.categories if c.id == category_id), None)
        self.categories.remove(cat)
        # del cat

    def delete_topic(self, topic_id):
        topic = next((t for t in self.topics if t.id == topic_id), None)
        self.topics.remove(topic)
        # del topic

    def delete_document(self, document_id):
        document = next((d for d in self.documents if d.id == document_id), None)
        # del document
        self.documents.remove(document)

    def get_document(self, document_id):
        return next((d for d in self.documents if d.id == document_id), None)

    def __repr__(self):
        result = '\n'.join([repr(d) for d in self.documents])
        return result

