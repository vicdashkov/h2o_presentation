import h2o
h2o.init()
from h2o.estimators.deeplearning import H2OAutoEncoderEstimator
from h2o.automl import H2OAutoML

housing_train_data_path = '/kaggle_datasets/data_files/housing_train.csv'
housing_train_data = h2o.import_file(housing_train_data_path)
splits = housing_train_data.split_frame(ratios=[0.9], seed=1)
house_train = splits[0]
house_test = splits[1]

aml = H2OAutoML(max_runtime_secs = 60 * 60 * 7)
aml.train(y="SalePrice",training_frame=house_train)
leader = aml.leader
first_four_no_price = house_test[0:4, 0:80]
prediction = leader.predict(first_four_no_price)
leader_path = h2o.save_model(model=leader, path='/kaggle_datasets/models', force=True)
print(leader_path)

print(prediction)
"""
real values:
118000
325300
82000
114500

automml with 60 * 60 * 7 (it ran for more than 8 hours)
128035
330030
88439
122528

automml with 9999 seconds(2 hours 45 minutes)
127389
323932
82803.7
129163

Default GBM
128682
316628
83699.2
129924

"""
