# Group 26: Movie Review Rating Predictor Pipeline
# author: Yuanzhe Marco Ma, Arash Shamseddini, Kaicheng Tan, Zhenrui Yu
# date: 2020-12-02

all : results/model_test_scores.csv results/histogram_rating_distribution.svg

# Download raw data
data/raw/Dataset_IMDB.csv : src/download_data.py
	# Download raw data from the original repository
	python src/download_data.py https://github.com/nproellochs/SentimentDictionaries/raw/master/Dataset_IMDB.csv data/raw/Dataset_IMDB.csv

# Generate resources for EDA
results/histogram_rating_distribution.svg results/boxplot_rating_critics.svg results/histogram_rating_vs_text_length.svg : src/eda_imdb.py data/raw/Dataset_IMDB.csv
	# Generate visualizations necessary for analysis reports
	python src/eda_imdb.py data/raw/Dataset_IMDB.csv results

# Pre-process data
data/processed/train.csv data/processed/test.csv : src/pre_process.py data/raw/Dataset_IMDB.csv
	# Pre-process data
	python src/pre_process.py --input_file=data/raw/Dataset_IMDB.csv --out_dir=data/processed

# Model tuning and fitting
results/model.pkl results/hyper_param_search_result.csv : src/imdb_rating_predict_model.py data/processed/train.csv
	# Generate and persist ML model
	python src/imdb_rating_predict_model.py data/processed/train.csv results

# Model evaluation
results/model_test_scores.csv results/true_vs_predict.html : src/imdb_rating_test_results.py results/model.pkl data/processed/test.csv
	# Evaluate the model with test set
	python src/imdb_rating_test_results.py results/model.pkl data/processed/test.csv results

# Clean intermediate files
clean :
	rm -rf data
	rm -rf results
