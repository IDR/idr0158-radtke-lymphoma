import omero
from omero.cli import cli_login
from omero.gateway import BlitzGateway

# This script will add an empty "Antibody Name" key-value pair
# to every MapAnnotation which doesn't have one. Additionally it
# will rename all "Antibody" keys to "Antibody Name"

with cli_login() as c:
    conn = BlitzGateway(client_obj=c.get_client())
    queryService = conn.getQueryService()
    params = omero.sys.Parameters()
    query = "select m from MapAnnotation m join m.mapValue mv where m.ns='openmicroscopy.org/mapr/antibody'"
    maps = conn.getQueryService().findAllByQuery(query, params)
    for i, map in enumerate(maps):
        nvs = map.getMapValue()
        id = None
        names = []
        update = False
        for nv in nvs:
            if nv.name == "Antibody Identifier":
                id = nv.value
            elif nv.name == "Antibody Name":
                names.append(nv.value)
            elif nv.name == "Antibody":
                nv.name = "Antibody Name"
                update = True
                names.append(nv.value)
        if len(names) == 0:
            nvs.append(omero.model.NamedValue("Antibody Name", ""))
            map.setMapValue(nvs)
            update = True
        if update:
            conn.getUpdateService().saveAndReturnObject(map)
        print(f"{i} - {id}")

