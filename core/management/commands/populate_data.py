from django.core.management.base import BaseCommand
from django.core.management.base import BaseCommand
from academics.models import Discipline, Branch, AcademicYear, Subject, StudyMaterial
from django.utils.text import slugify

class Command(BaseCommand):
    help = 'Populates initial data for Disciplines, Branches, and Years'

    def handle(self, *args, **kwargs):
        self.stdout.write('Populating data...')
        
        # 1. Academic Years
        years = ['1st Year', '2nd Year', '3rd Year', '4th Year']
        for i, y in enumerate(years, 1):
            AcademicYear.objects.get_or_create(year=i, defaults={'name': y})

        # Data Structure: Discipline -> Branch -> Year -> [(Subject, Desc)]
        # Based on typical AICTE/UGC Model Curriculum
        curriculum = {
            'Engineering': {
                'Common': { # Applied to 1st year of all Engg
                    1: [
                        ('Engineering Physics', 'Optics, Lasers, Quantum Mechanics, and Solid State Physics.'),
                        ('Engineering Mathematics-I', 'Calculus, Matrices, and Differential Equations.'),
                        ('Basic Electrical Engineering', 'DC Circuits, AC Circuits, Transformers, and Machines.'),
                        ('Engineering Graphics', 'Projections, Isometric Views, and CAD basics.'),
                        ('Programming for Problem Solving', 'C Programming, Algorithms, and Flowcharts.')
                    ]
                },
                'Computer Science': {
                    2: [('Data Structures', 'Arrays, Linked Lists, Trees, Graphs.'), ('Digital Electronics', 'Boolean Algebra, Logic Gates, Combinational Circuits.'), ('Discrete Mathematics', 'Set Theory, Graph Theory, Combinatorics.'), ('COA', 'Computer Organization and Architecture.'), ('OOP', 'Object Oriented Programming using C++/Java.')],
                    3: [('Database Management Systems', 'SQL, Normalization, Transactions.'), ('Operating Systems', 'Process Management, Memory Management, File Systems.'), ('Theory of Computation', 'Automata, Context Free Grammars, Turing Machines.'), ('Computer Networks', 'OSI Model, TCP/IP, Routing, Switching.'), ('Software Engineering', 'SDLC, Agile, Testing, Project Management.')],
                    4: [('Compiler Design', 'Lexical Analysis, Parsing, Code Optimization.'), ('Artificial Intelligence', 'Search Algorithms, Knowledge Representation, ML basics.'), ('Cloud Computing', 'AWS, Azure, Virtualization, Containers.'), ('Information Security', 'Cryptography, Network Security, Cyber Laws.'), ('Project Phase-II', 'Final Year Major Project implementation.')]
                },
                'Information Technology': {
                    2: [('Data Structures & Files', 'Advanced DS, Hashing, File Handling.'), ('Digital Logic Design', 'Number Systems, Karnaugh Maps, Sequential Circuits.'), ('Discrete Structures', 'Logic, Relations, Functions, Recurrence Relations.'), ('Computer Graphics', '2D/3D Transformations, Clipping, Rendering.'), ('Processor Architecture', '8086/80386 Architecture, Assembly Language.')],
                    3: [('Database Systems', 'Relational Model, SQL, NoSQL, PL/SQL.'), ('Operating System Concepts', 'Threads, Scheduling, Deadlocks, Virtual Memory.'), ('Human Computer Interaction', 'UI/UX Design Principles, Usability Testing.'), ('Computer Network Technology', 'Physical, Data Link, Network, Transport Layers.'), ('Web Technology', 'HTML, CSS, JS, PHP, Servlets.')],
                    4: [('Data Analytics', 'Big Data, Hadoop, Data Visualization.'), ('Machine Learning', 'Supervised/Unsupervised Learning, Neural Networks.'), ('Cyber Security', 'Threats, Vulnerabilities, IDPS, Firewalls.'), ('Distributed Systems', 'RPC, RMI, Distributed Shared Memory, Consensus.'), ('Project Phase-II', 'Final Year Major Project.')]
                },
                'Electronics & Telecommunication': {
                    2: [('Electronic Circuits', 'Diodes, BJTs, MOSFETs, Amplifiers.'), ('Digital Circuits', 'Logic Families, Combinational/Sequential Circuits.'), ('Electrical Circuits', 'Network Theorems, Transient Analysis.'), ('Data Structures & Algorithms', 'C++, Stacks, Queues, Sorting.'), ('Signals & Systems', 'CT/DT Signals, Fourier/Laplace/Z Transforms.')],
                    3: [('Digital Communication', 'PCM, DM, ASK, FSK, PSK, Information Theory.'), ('Microcontrollers', '8051, PIC, ARM, Embedded C.'), ('Electromagnetics', 'Maxwell Equations, Transmission Lines, Waveguides.'), ('Digital Signal Processing', 'DFT, FFT, Digital Filter Design.'), ('Control Systems', 'Time/Frequency Response, Stability Analysis.')],
                    4: [('VLSI Design', 'CMOS, Layout, VHDL/Verilog, FPGA.'), ('Mobile Communication', 'GSM, CDMA, LTE, 5G Fundamentals.'), ('Microwave Engineering', 'Waveguides, Antennas, Radar Systems.'), ('Embedded Systems Design', 'RTOS, IoT, Device Drivers.'), ('Project Phase-II', 'Hardware/Software Co-design Project.')]
                },
                'Civil': {
                    2: [('Strength of Materials', 'Stress, Strain, Bending Moments, Deflection.'), ('Fluid Mechanics', 'Fluid Properties, Statics, Kinematics, Dynamics.'), ('Surveying', 'Theodolite, Levelling, Contouring, Total Station.'), ('Building Materials & Construction', 'Stones, Bricks, Cement, Concrete, Masonry.'), ('Engineering Geology', 'Rocks, Minerals, Earthquakes, Maps.')],
                    3: [('Structural Analysis', 'Indeterminate Structures, Arches, Bridges.'), ('Geotechnical Engineering', 'Soil Properties, Foundations, Shear Strength.'), ('Environmental Engineering', 'Water Supply, Waste Water Treatment, Pollution.'), ('Transportation Engineering', 'Highway Design, Traffic Engineering, Pavements.'), ('Concrete Technology', 'Mix Design, Admixtures, Special Concretes.')],
                    4: [('Design of Concrete Structures', 'RCC, Beams, Slabs, Columns, Footings.'), ('Construction Management', 'PERT, CPM, Project Planning, Safety.'), ('Irrigation Engineering', 'Dams, Canals, Hydrology, Water Resources.'), ('Estimation & Costing', 'Rate Analysis, Tendering, Valuation.'), ('Project Phase-II', 'Structure Design/Civil Infrastructure Project.')]
                },
                'Mechanical': {
                    2: [('Thermodynamics', 'Laws of Thermodynamics, Entropy, Cycles.'), ('Fluid Mechanics & Machinery', 'Fluid Statics, Dynamics, Pumps, Turbines.'), ('Material Science', 'Properties of Materials, Heat Treatment, Alloys.'), ('Manufacturing Processes', 'Casting, Welding, Machining, Forming.'), ('Kinematics of Machinery', 'Mechanisms, Cams, Gears, Motion Analysis.')],
                    3: [('Heat Transfer', 'Conduction, Convection, Radiation, Heat Exchangers.'), ('Dynamics of Machinery', 'Balancing, Vibration, Gyroscope.'), ('Machine Design', 'Design of Shafts, Bearings, Gears, Springs.'), ('Metrology & Quality Control', 'Measurements, Limits, Fits, SQC, ISO.'), ('Turbo Machines', 'Steam Turbines, Gas Turbines, Compressors.')],
                    4: [('Refrigeration & Air Conditioning', 'Psychrometry, Refrigerants, Load Calculation.'), ('CAD/CAM/CAE', 'Geometric Modeling, NC/CNC, FEA.'), ('Automobile Engineering', 'Chassis, Engine, Transmission, Suspension.'), ('Power Plant Engineering', 'Thermal, Hydro, Nuclear, Renewable Power.'), ('Project Phase-II', 'Design/Fabrication Project.')]
                },
                'Electrical': {
                    2: [('Analog Electronics', 'Diodes, Transistors, Op-Amps, Oscillators.'), ('Electrical Machines-I', 'DC Generators, DC Motors, Transformers.'), ('Circuit Analysis', 'Network Theorems, Graph Theory, Two-port Networks.'), ('Electromagnetic Fields', 'Vector Analysis, Electrostatics, Magnetostatics.'), ('Digital Electronics', 'Logic Gates, Combinational/Sequential Circuits.')],
                    3: [('Power Systems-I', 'Generation, Transmission, Distribution.'), ('Electrical Machines-II', 'Induction Motors, Synchronous Machines.'), ('Control Systems', 'Time/Frequency Domain, Stability, PID.'), ('Power Electronics', 'SCR, Converters, Inverters, Choppers.'), ('Microprocessors', '8085, 8086 Architecture, Interfacing.')],
                    4: [('Switchgear & Protection', 'Circuit Breakers, Relays, Protection Schemes.'), ('Electrical Drives', 'DC/AC Drives, Traction.'), ('High Voltage Engineering', 'Breakdown, HV Generation, measurement.'), ('Smart Grid Technology', 'Graph Theory, AMI, IoT in Power.'), ('Project Phase-II', 'Power/Control System Project.')]
                },
                'Chemical': {
                    2: [('Chemical Process Calculations', 'Stoichiometry, Material Balance, Energy Balance.'), ('Fluid Flow', 'Reynolds Number, Piping, Pumps, Flow Meters.'), ('Chemical Engineering Thermodynamics', 'Laws, Phase Equilibria, Chemical Potential.'), ('Mechanical Operations', 'Crushing, Grinding, Filtration, Mixing.'), ('Inorganic Chemical Technology', 'Acids, Alkalis, Fertilizers, Cement.')],
                    3: [('Heat Transfer', 'Conduction, Convection, Heat Exchangers.'), ('Mass Transfer-I', 'Diffusion, Distillation, Absorption.'), ('Chemical Reaction Engineering-I', 'Kinetics, Ideal Reactors, Batch/CSTR/PFR.'), ('Material Science', 'Corrosion, Ceramics, Polymers.'), ('Process Instrumentation', 'Measurement of T, P, Flow, Level.')],
                    4: [('Process Dynamics & Control', 'Feedback Control, Stability, Tuning.'), ('Plant Design & Economics', 'Process Design, Cost Estimation, Profitability.'), ('Transport Phenomena', 'Momentum, Heat, Mass Transfer Analogies.'), ('Environmental Engineering', 'Pollution Control, waste management.'), ('Project Phase-II', 'Chemical Process Project.')]
                },
                'Aerospace': {
                    2: [('Aerodynamics-I', 'Fluid Dynamics, Airfoils, Lift, Drag.'), ('Aircraft Structures-I', 'Stress Analysis, Beams, Trusses, Materials.'), ('Flight Mechanics-I', 'Performance, Climbing, Gliding, Range.'), ('Propulsion-I', 'Thermodynamics of Propulsion, piston engines.'), ('Space Science', 'Solar System, Orbital Mechanics basics.')],
                    3: [('Aerodynamics-II', 'Compressible Flow, Shock Waves, Nozzles.'), ('Aircraft Structures-II', 'Plates, Shells, Fatigue, Fracture Mechanics.'), ('Propulsion-II', 'Jet Engines, Turbojet, Turbofan, Ramjet.'), ('Control Engineering', 'Flight Control Systems, Stability.'), ('Avionics', 'Radar, Navigation, Cockpit Systems.')],
                    4: [('Rocket Propulsion', 'Solid/Liquid Propellants, Nozzles, Thrust.'), ('Computational Fluid Dynamics', 'Discretization, FDM, FVM.'), ('Satellite Technology', 'Orbit Control, Payloads, Launch Vehicles.'), ('Helicopter Dynamics', 'Rotor Aerodynamics, Hover, Vertical Flight.'), ('Project Phase-II', 'Design/Analysis Project.')]
                },
            },
            'Science': {
                'Physics': {
                    1: [('Mechanics', 'Laws of Motion, Energy, Rotational Dynamics.'), ('Electricity & Magnetism', 'Electric Fields, Circuits, Magnetism.'), ('Mathematical Physics', 'Vector Calculus, Matrices, Differential Equations.'), ('Chemistry-I', 'Physical and Organic Chemistry basics.')],
                    2: [('Thermal Physics', 'Thermodynamics, Kinetic Theory, Statistical Mechanics.'), ('Waves & Optics', 'Interference, Diffraction, Polarization.'), ('Analog Electronics', 'Diodes, Transistors, Op-Amps.'), ('Nuclear Physics', 'Radioactivity, Fission, Fusion.')],
                    3: [('Quantum Mechanics', 'Schrodinger Equation, Operators, Hydrogen Atom.'), ('Condensed Matter Physics', 'Crystal Structure, Band Theory, Superconductivity.'), ('Atomic & Molecular Physics', 'Spectroscopy, Laser Physics.'), ('Astrophysics', 'Stars, Galaxies, Cosmology.')]
                },
                'Chemistry': {
                     1: [('Inorganic Chemistry-I', 'Periodic Table, Bonding.'), ('Organic Chemistry-I', 'Stereochemistry, Hydrocarbons.'), ('Physical Chemistry-I', 'Gases, Thermodynamics.')],
                     2: [('Inorganic Chemistry-II', 'Coordination Compounds, d-block.'), ('Organic Chemistry-II', 'Alcohols, Phenols, Carbonyls.'), ('Physical Chemistry-II', 'Equilibrium, Electrochemistry.')],
                     3: [('Analytical Chemistry', 'Spectroscopy, Chromatography.'), ('Industrial Chemistry', 'Dyes, Drugs, Polymers.'), ('Environmental Chemistry', 'Pollution, Green Chemistry.')]
                },
                'Mathematics': {
                    1: [('Calculus', 'Limits, Continuity, Differentiation, Integration.'), ('Algebra', 'Groups, Rings, Fields.'), ('Differential Equations', 'ODE, PDE, Laplace Transforms.')],
                    2: [('Real Analysis', 'Sequences, Series, Convergence.'), ('Linear Algebra', 'Vector Spaces, Linear Transformations.'), ('Numerical Analysis', 'Interpolation, Numerical Integration.')],
                    3: [('Complex Analysis', 'Analytic Functions, Residues.'), ('Topology', 'Metric Spaces, Topological Spaces.'), ('Operations Research', 'LPP, Simplex, Transport Problem.')]
                }
            },
            'Commerce': {
                'B.Com': {
                    1: [('Financial Accounting', 'Accounting Principles, Ledger, Trial Balance.'), ('Business Economics', 'Demand, Supply, Market Structures.'), ('Business Mathematics', 'Calculus, Matrices, Commercial Math.'), ('Business Communication', 'Skills, Drafting, Reports.')],
                    2: [('Corporate Accounting', 'Company Accounts, Valuation, Liquidation.'), ('Cost Accounting', 'Cost Sheet, Material/Labor Cost, Overheads.'), ('Business Law', 'Contract Act, Sale of Goods, Consumer Protection.'), ('Income Tax Law', 'Heads of Income, Deductions.')],
                    3: [('Auditing & Taxation', 'Income Tax, GST, Audit Procedures.'), ('Management Accounting', 'Ratio Analysis, Cash Flow, Budgeting.'), ('Banking & Finance', 'Banking Structure, Financial Markets, Instruments.'), ('Entrepreneurship', 'Business Plans, Startups, MSME.')]
                }
            },
            'Arts': {
                'History': {
                    1: [('Ancient India', 'Indus Valley to Guptas.'), ('Medieval India', 'Sultanate, Mughals.'), ('World History', 'Renaissance, French Revolution.')],
                    2: [('Modern India', 'British Rule, Freedom Struggle.'), ('History of Europe', 'Napoleonic Era, World Wars.'), ('Tourism', 'Heritage Sites, Guide Skills.')],
                    3: [('Post Independence India', 'Partition, Constitution, Planning.'), ('Historiography', 'Methods, Sources, Historians.'), ('Archaeology', 'Excavation, Dating methods.')]
                },
                'Political Science': {
                    1: [('Political Theory', 'State, Sovereignty, Rights, Justice.'), ('Indian Government', 'Constitution, Parliament, Judiciary.'), ('International Relations', 'Cold War, UN, Foreign Policy.')],
                    2: [('Western Political Thought', 'Plato, Aristotle, Machiavelli, Marx.'), ('Comparative Politics', 'UK, USA, China constitutions.'), ('Public Administration', 'Bureaucracy, Budgeting, Governance.')],
                    3: [('Indian Political Thought', 'Gandhi, Ambedkar, Kautilya.'), ('Local Self Government', 'Panchayati Raj, Municipalities.'), ('Human Rights', 'UDHR, NHRC, Issues.')]
                }
            },
            'Diploma': {
                'Computer Engineering': {
                     1: [('Basic Physics', 'Measurement, Mechanics, Heat.'), ('Basic Chemistry', 'Atomic Structure, Electrochemistry.'), ('Basic Mathematics', 'Algebra, Trigonometry.'), ('Engineering Graphics', 'Projections, Lines, Planes.'), ('Computer Fundamentals', 'Hardware, Software, OS basics.')],
                     2: [('Programming in C', 'Syntax, Loops, Arrays, Functions.'), ('Digital Techniques', 'Number systems, Gates, Flip-flops.'), ('Electrical Tech', 'Circuits, Motors, Transformers.'), ('Web Page Design', 'HTML, CSS basics.')],
                     3: [('Object Oriented Programming', 'C++, Classes, Objects.'), ('Data Structures', 'Arrays, Stacks, Queues.'), ('Computer Networks', 'OSI model, Network devices.'), ('Database Management', 'RDBMS concepts, SQL.')]
                },
                'Mechanical Engineering': {
                     1: [('Basic Physics', 'Measurement, Mechanics, Heat.'), ('Basic Chemistry', 'Metals, Alloys, Corrosion.'), ('Basic Mathematics', 'Algebra, Coordinate Geometry.'), ('Engineering Graphics', 'Projections, Sections.'), ('Engineering Workshop', 'Carpentry, Fitting, Smithy.')],
                     2: [('Applied Mechanics', 'Forces, Moments, Friction.'), ('Mechanical Drawing', 'Assembly drawing, Fits, Tolerances.'), ('Thermal Engineering', 'Boilers, Engines, Compressors.'), ('Manufacturing Processes', 'Lathe, Drilling, Milling.')],
                     3: [('Strength of Materials', 'Stress, Strain, Torsion, Beams.'), ('Theory of Machines', 'Kinematics, Cams, Power transmission.'), ('Fluid Mechanics', 'Properties, Bernoulli eqn, Pumps.'), ('Metrology', 'Measurement standards, Gauges.')]
                }
            }
        }

        # Populate
        # Helper to generate syllabus
        def get_syllabus(subject_name):
            return f"""
**Unit 1: Introduction to {subject_name}**
- Basic Concepts and Definitions
- Historical Development
- Fundamental Principles
- Scope and Applications

**Unit 2: Core Theories and Models**
- Key Theoretical Frameworks
- Mathematical Formulations
- Analysis of Primary Components
- Standard Standards and Conventions

**Unit 3: Advanced Topics**
- Complex Systems and Interactions
- Modern Techniques and Tools
- Computational Methods
- Optimization Strategies

**Unit 4: Specialized Applications**
- Case Studies in Industry/Research
- Emerging Trends and Innovations
- Integration with other Disciplines
- Real-world Problem Solving

**Unit 5: Practical Implementation**
- Laboratory/Field Techniques
- Design and Simulation
- Project Planning and Execution
- Regulatory and Ethical Considerations

**Unit 6: Revision and Future Scope**
- Review of Key Concepts
- Challenges and Open Problems
- Future Directions in {subject_name}
"""

        # Populate
        from academics.models import StudyMaterial

        for discipline_name, branches_data in curriculum.items():
            disc, _ = Discipline.objects.get_or_create(name=discipline_name, defaults={'slug': slugify(discipline_name)})
            
            # Handle "Common" subjects for Engineering
            common_data = branches_data.pop('Common', {}) if discipline_name == 'Engineering' else {}

            for branch_name, years_data in branches_data.items():
                branch, _ = Branch.objects.get_or_create(discipline=disc, name=branch_name, defaults={'slug': slugify(branch_name)})
                self.stdout.write(f'Processing {branch_name}...')

                # Add Common 1st Year subjects if Engineering
                if discipline_name == 'Engineering' and common_data:
                    year_1 = AcademicYear.objects.get(year=1)
                    for sub, desc in common_data[1]:
                        subject, created = Subject.objects.get_or_create(
                            branch=branch, academic_year=year_1, name=sub,
                            defaults={'code': f'{slugify(sub)[:3].upper()}101', 'description': desc, 'syllabus_text': get_syllabus(sub)}
                        )
                        # Add demo materials
                        if created:
                            StudyMaterial.objects.create(subject=subject, title=f'{sub} Syllabus', type='syllabus', link='https://example.com/syllabus.pdf', description='Official Syllabus')
                            StudyMaterial.objects.create(subject=subject, title=f'Introduction to {sub}', type='note', link='https://example.com/notes.pdf', description='Chapter 1 Notes')

                # Add Specific Years
                for year_num, subjects in years_data.items():
                    year_obj = AcademicYear.objects.get(year=year_num)
                    for i, (sub, desc) in enumerate(subjects):
                        code = f'{slugify(branch_name)[:2].upper()}{year_num}0{i+1}'
                        subject, created = Subject.objects.get_or_create(
                            branch=branch, academic_year=year_obj, name=sub,
                            defaults={'code': code, 'description': desc, 'syllabus_text': get_syllabus(sub)}
                        )
                        # Add demo materials
                        if created:
                             StudyMaterial.objects.create(subject=subject, title=f'{sub} Detailed Syllabus', type='syllabus', link='https://example.com/syllabus.pdf', description='Detailed University Syllabus')
                             StudyMaterial.objects.create(subject=subject, title=f'{sub} Reference Book', type='book', link='https://example.com/book.pdf', description='Standard Reference Book')
                             StudyMaterial.objects.create(subject=subject, title=f'Video Lecture: {sub}', type='video', link='https://youtube.com/watch?v=demo', description='Introductory Video Lecture')

        self.stdout.write(self.style.SUCCESS('Successfully populated comprehensive curriculum data with study materials'))
