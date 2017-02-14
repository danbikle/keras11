# keras12.py

# This script should use Keras and Flask-RESTful to generate stock market predictions.

# Demo:
# export FLASK_DEBUG=1
# ~/anaconda3/bin/python keras12.py

import keras11
import io
import keras
import pdb
import os
import flask         as fl
import flask_restful as fr
import numpy         as np

application = fl.Flask(__name__)
api         = fr.Api(application)

class Nnmodel(fr.Resource):
  # This method should create a model to predict yr2predict.
  def get(self,local=False, tkr='SPY',yr2predict='2017',yrs2train=10,hlayers=1,neurons=4,features='pctlag1,slope2,moy'):      
    # I should get prices and features for tkr:
    if not local: # I should see fl.request.args
      features = fl.request.args.get('features', 'pctlag1,slope3,dom')
    features_l = features.split(',')
    col_l      = ['cdate','closep','pctlead','updown']+features_l

    feat_df    = keras11.genf(tkr)[col_l]

    # I should copy test_yr-observations (about 252) from feat_df into test_yr_df.
    test_start_sr = (feat_df.cdate > yr2predict)
    test_end_sr   = (feat_df.cdate < str(int(yr2predict)+1))
    test_yr_df    = feat_df.copy()[(test_start_sr & test_end_sr)]

    # I should copy train_i-years of observations before test_yr from feat_df into train_df
    train_i        = yrs2train
    train_end_sr   = (feat_df.cdate < yr2predict)
    train_start_i  = int(yr2predict) - train_i
    train_start_s  = str(train_start_i)
    train_start_sr = (feat_df.cdate > train_start_s)
    train_df       = feat_df.copy()[ train_start_sr & train_end_sr ]
    
    # I should declare x_train to be train_df.pctlag1
    x_train = train_df[features_l].fillna(0.0)
    # I should declare y_train to be train_df.pctlead
    y_train = train_df.pctlead
    # I should use model to "fit" straight line to x_train and y_train
    x_train_a = np.array(x_train)
    y_train_a = np.array(y_train)
    # I should use Keras to fit a model here.
    # Keras kmodel wants a 1-hot encoded class.
    ytrain1h_l = [[0,1] if updown else [1,0] for updown in train_df.updown]
    ytrain1h_a = np.array(ytrain1h_l).reshape(-1,2)
    kmodel     = keras.models.Sequential()
    features_i = len(features_l)
    kmodel.add(keras.layers.core.Dense(neurons, input_shape=(features_i,)))
    kmodel.add(keras.layers.core.Activation('relu'))
    # hlayers should be 1, 2, 3, 4
    if hlayers < 1:
      return {'badnews':'hlayers < 1'}
    if hlayers > 4:
      return {'badnews':'hlayers > 4'}
    
    pdb.set_trace()    
    return {'nothing':'yet'}

api.add_resource(Nnmodel, '/nnmodel/<tkr>/<yr2predict>/<int:yrs2train>/<int:hlayers>/<int:neurons>')
# curl localhost:5012/nnmodel/IBM/2017/3/2/3?features=pctlag1,slope2,dow,moy

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5012))
    application.run(host='0.0.0.0', port=port)
'bye'

