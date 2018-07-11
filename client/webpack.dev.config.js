const Webpack = require("webpack")
const path = require("path")
const { VueLoaderPlugin } = require('vue-loader')

module.exports = {
	entry:"./src/main.js",
	output:{
		path:path.resolve(__dirname, 'dist'),
		filename:"app.min.js"
	},
	module:{
		rules:[
			{ test: /\.(js|jsx)/, loader: 'babel-loader', exclude: /(node_modules)/ },
            { test: /\.css$/, loader: 'style-loader!css-loader' },
            { test: /\.(png|jpg)$/, loader: 'url-loader' },
            { test: /\.(eot|svg|ttf|woff)$/, loader: 'url-loader' },
            { test: /\.vue/, loader: 'vue-loader' }
		]
	},
	plugins: [
		new VueLoaderPlugin()
	]
}