module.exports = function (grunt) {
  require('jit-grunt')(grunt);

  grunt.initConfig({
    jshint: {
      options: {
        reporter: require('jshint-stylish')
      },
      build: ['Grunfile.js', 'src/**/*.js']
    },
    uglify: {
      build: {
        files: {
          'dest/js/form.js': 'src/js/form.js',
          'dest/js/management.js': 'src/js/management.js',
          'dest/js/routing.js': 'src/js/routing.js'
        }
      }
    },
    watch: {
      // for stylesheets, watch css and less files
      // only run less and cssmin stylesheets: {
      files: ['src//*.css', 'src//*.less'],
      tasks: ['less', 'cssmin']
    },
    connect: {
      server: {
        options: {
          port: 8000,
          base: 'app',
          keepalive: false
        }
      }
    },
    less: {
      build: {
        files: {
          'dest/style.css': 'src/style.less'
        }
      }
    }
  });

  grunt.registerTask('default', ['jshint', 'uglify', 'less', 'connect', 'watch']);
};
