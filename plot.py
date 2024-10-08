from shapely.geometry import Polygon


def plot_polygon(ax, poly, label=None, **kwargs):
    x, y = poly.exterior.xy
    ax.fill(x, y, label=label, **kwargs)
    return


def plot_shapes(ax, polygons, colors, **kwargs):
    for poly, color in zip(polygons, colors):
        plot_polygon(ax, Polygon(poly), color=color, **kwargs)