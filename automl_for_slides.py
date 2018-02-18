import h2o
from h2o.automl import H2OAutoML
h2o.init()

aml = H2OAutoML(max_runtime_secs=3600)  # 1 hour
aml.train(y="SalePrice", training_frame=h2o.import_file('/housing_train.csv'))

leader = aml.leader
prediction = leader.predict(h2o.import_file('/housing_predict.csv'))