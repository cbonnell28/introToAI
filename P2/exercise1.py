from pgmpy.models import BayesianModel
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

# Defining the model structure. We can define the network by just passing a list of edges.
model = BayesianModel([('B', 'G'), ('F', 'G')])

# Defining individual CPDs.
cpd_b = TabularCPD(variable='B', variable_card=2, values=[[0.2, 0.8]])
cpd_f = TabularCPD(variable='F', variable_card=2, values=[[0.1, 0.9]])

# The representation of CPD in pgmpy is a bit different than the CPD shown in the above picture. In pgmpy the colums
# are the evidences and rows are the states of the variable. So the grade CPD is represented like this:
#
#    +---------+---------+---------+---------+---------+
#    | diff    | intel_0 | intel_0 | intel_1 | intel_1 |
#    +---------+---------+---------+---------+---------+
#    | intel   | diff_0  | diff_1  | diff_0  | diff_1  |
#    +---------+---------+---------+---------+---------+
#    | grade_0 | 0.3     | 0.05    | 0.9     | 0.5     |
#    +---------+---------+---------+---------+---------+
#    | grade_1 | 0.4     | 0.25    | 0.08    | 0.3     |
#    +---------+---------+---------+---------+---------+
#    | grade_2 | 0.3     | 0.7     | 0.02    | 0.2     |
#    +---------+---------+---------+---------+---------+

cpd_g = TabularCPD(variable='G', variable_card=2, 
                   values=[[0.9, 0.9, 0.8,  0.1],
                           [0.1, 0.1,  0.2, 0.9]],
                  evidence=['F', 'B'],
                  evidence_card=[2, 2])


# Associating the CPDs with the network
model.add_cpds(cpd_b, cpd_f, cpd_g)

# check_model checks for the network structure and CPDs and verifies that the CPDs are correctly 
# defined and sum to 1.
model.check_model()
# These defined CPDs can be added to the model. Since, the model already has CPDs associated to variables, it will
# show warning that pmgpy is now replacing those CPDs with the new ones.
model.get_cpds()
print(cpd_g)
infer = VariableElimination(model)
print(infer.query(['G']))
