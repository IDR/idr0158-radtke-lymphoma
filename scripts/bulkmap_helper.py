

for i in range(1, 41):
    print(f"  - group:")
    print(f"      namespace: openmicroscopy.org/mapr/antibody")
    print(f"      columns:")
    print(f"        - name: Experimental Condition [Primary Antibody {i}]")
    print(f"          clientname: Antibody")
    print(f"          include: true")
    print(f"        - name: Primary Antibody {i} Identifier")
    print(f"          clientname: Antibody Identifier")
    print(f"          include: true")
    print(f"        - name: Primary Antibody {i} Identifier")
    print(f"          clientname: Antibody Identifier URL")
    print(f"          clientvalue: http://antibodyregistry.org/{{ value|urlencode }}")
    print(f"          include: true")

print("===========================")

for i in range(1, 41):
    print(f"        - name: Primary Antibody {i} Identifier")
    print(f"          clientname: Antibody {i} Identifier")
    print(f"          include: true")
    print(f"        - name: Primary Antibody {i} Dilution")
    print(f"          clientname: Antibody {i} Dilution")
    print(f"          include: true")
