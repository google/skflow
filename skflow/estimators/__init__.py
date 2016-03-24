"""Scikit Flow Estimators."""
#  Copyright 2015-present Scikit Flow Authors. All Rights Reserved.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

from skflow.estimators.base import TensorFlowEstimator
from skflow.estimators.linear import TensorFlowLinearClassifier
from skflow.estimators.linear import TensorFlowClassifier
from skflow.estimators.linear import TensorFlowLinearRegressor
from skflow.estimators.linear import TensorFlowRegressor
from skflow.estimators.dnn import TensorFlowDNNClassifier
from skflow.estimators.dnn import TensorFlowDNNRegressor
from skflow.estimators.rnn import TensorFlowRNNClassifier
from skflow.estimators.rnn import TensorFlowRNNRegressor
from skflow.estimators.stacked_autoencoder import StackedAutoEncoder
from skflow.estimators.basic_autoencoder import BasicAutoEncoder
