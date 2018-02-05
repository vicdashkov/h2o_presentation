import h2o
h2o.init()
from h2o.estimators.deeplearning import H2OAutoEncoderEstimator
from h2o.automl import H2OAutoML

housing_train_data_path = 'https://raw.githubusercontent.com/vicdashkov/kaggle_datasets/master/housing_train.csv'
housing_train_data = h2o.import_file(housing_train_data_path)
splits = housing_train_data.split_frame(ratios=[0.9], seed=1)
house_train = splits[0]
house_test = splits[1]

aml = H2OAutoML(max_runtime_secs = 9999)
aml.train(y="SalePrice",training_frame=house_train)
leader = aml.leader
first_four_no_price = house_test[0:4, 0:80]
first_four_no_price
prediction = leader.predict(first_four_no_price)
print(prediction)
"""
This predicted 

  predict
---------
 127389
 323932
  82803.7
 129163


with GBM
And this is better than GBM with standard params
"""
