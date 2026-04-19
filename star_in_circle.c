#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <cairo.h>
#include <cairo-svg.h>

#define WIDTH 400
#define HEIGHT 400
#define RADIUS 150
#define CX 200
#define CY 200

void draw_star_in_circle(const char *filename) {
    cairo_surface_t *surface = cairo_svg_surface_create(filename, WIDTH, HEIGHT);
    cairo_t *cr = cairo_create(surface);

    // Background
    cairo_set_source_rgb(cr, 1, 1, 1);
    cairo_paint(cr);

    // Draw circle
    cairo_set_source_rgb(cr, 0, 0, 0);
    cairo_set_line_width(cr, 2);
    cairo_arc(cr, CX, CY, RADIUS, 0, 2 * M_PI);
    cairo_stroke(cr);

    // Draw first triangle
    cairo_set_source_rgb(cr, 1, 0, 0);
    cairo_set_line_width(cr, 2);
    cairo_move_to(cr, CX + RADIUS * cos(M_PI/2), CY - RADIUS * sin(M_PI/2));
    for (int i = 1; i < 3; ++i) {
        double angle = M_PI/2 + i * 2 * M_PI / 3;
        cairo_line_to(cr, CX + RADIUS * cos(angle), CY - RADIUS * sin(angle));
    }
    cairo_close_path(cr);
    cairo_stroke(cr);

    // Draw second triangle (rotated by 60 degrees)
    cairo_move_to(cr, CX + RADIUS * cos(M_PI/2 + M_PI/6), CY - RADIUS * sin(M_PI/2 + M_PI/6));
    for (int i = 1; i < 3; ++i) {
        double angle = M_PI/2 + M_PI/6 + i * 2 * M_PI / 3;
        cairo_line_to(cr, CX + RADIUS * cos(angle), CY - RADIUS * sin(angle));
    }
    cairo_close_path(cr);
    cairo_stroke(cr);

    cairo_destroy(cr);
    cairo_surface_destroy(surface);
}

int main() {
    draw_star_in_circle("star_in_circle.svg");
    printf("SVG file 'star_in_circle.svg' created.\n");
    return 0;
}
