package thevoiceless.resmath

import org.gradle.api.Plugin
import org.gradle.api.Project

class ResourceMathPlugin implements Plugin<Project> {

    void apply(Project project) {
        project.task('todo') << {
            println "TODO"
        }
    }
}
