import ifcopenshell
import numpy as np

def load_ifc(file_path):
    """Load an IFC file using ifcopenshell."""
    return ifcopenshell.open(file_path)

def detect_clashes(model):
    """Detect clashes between elements in the BIM model."""
    clashes = []
    elements = model.by_type("IfcBuildingElement")
    
    for i, elem1 in enumerate(elements):
        for elem2 in elements[i+1:]:
            if check_collision(elem1, elem2):
                clashes.append((elem1, elem2))
    
    return clashes

def check_collision(elem1, elem2):
    """Check if two elements collide using bounding boxes."""
    bbox1 = get_bounding_box(elem1)
    bbox2 = get_bounding_box(elem2)
    
    return not (bbox1[1][0] < bbox2[0][0] or bbox1[0][0] > bbox2[1][0] or
                bbox1[1][1] < bbox2[0][1] or bbox1[0][1] > bbox2[1][1] or
                bbox1[1][2] < bbox2[0][2] or bbox1[0][2] > bbox2[1][2])

def get_bounding_box(element):
    """Get the bounding box of an element."""
    geometry = ifcopenshell.geom.create_shape(settings, element)
    verts = np.array(geometry.geometry.verts).reshape(-1, 3)
    return (np.min(verts, axis=0), np.max(verts, axis=0))

if __name__ == "__main__":
    # Load the IFC model
    model = load_ifc("sample_model.ifc")
    
    # Detect clashes
    clashes = detect_clashes(model)
    
    # Print results
    print(f"Detected {len(clashes)} clashes:")
    for clash in clashes:
        print(f"Clash between {clash[0].Name} and {clash[1].Name}")