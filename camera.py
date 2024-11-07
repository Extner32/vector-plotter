from xvec_lib import vec3

def project_vertex(camera, vertex:vec3):

    #transform vertex to cam space
    transformed_vertex = vertex - camera.position
    transformed_vertex = rotate_point(transformed_vertex, camera.rotation)


    #perspective project the vertex
    projected_vertex = [0, 0]

    projected_vertex[0] = (transformed_vertex[0] * aspect_ratio * camera.near)/(transformed_vertex[2] + elipson)
    projected_vertex[1] = (-transformed_vertex[1] * camera.near)/(transformed_vertex[2] + elipson)

    #normalize the screen space
    projected_vertex[0] = (projected_vertex[0] + 1)/2
    projected_vertex[1] = (projected_vertex[1] + 1)/2

    projected_vertex = np.array(projected_vertex)

    return projected_vertex