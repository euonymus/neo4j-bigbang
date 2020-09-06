from repositories.csv_2_relationship_frame import Csv2RelationshipFrame
from business_rules.activate_relationship_frame import ActivateRelationship

class ActivateRelationships():
    def __init__(self, file_path, type_in_row = True, create_node = False):
        self.file_path = file_path
        self.type_in_row = type_in_row
        self.create_node = create_node

    def invoke(self):
        csv_2_relationship_frames = Csv2RelationshipFrame(self.file_path, self.type_in_row)
        relationship_frames = csv_2_relationship_frames.relationship_frames()

        ret = []
        for relationship_frame in relationship_frames:
            activate_relationship = ActivateRelationship(relationship_frame, self.create_node)
            relationship = activate_relationship.invoke()
            if relationship:
                ret.append(relationship)

        return ret
