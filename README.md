# vpype-dxf
 vpype dxf loading plugin

Adds command dread (dxf-read) that reads dxf files and into the vpype pipeline.

See: https://github.com/abey79/vpype for vpype.

# ezdxf

Ezdxf is used as the backend of this project. The `-Q`/`--query` feed directly into the [query field](https://ezdxf.readthedocs.io/en/stable/usage_for_beginners.html#query-dxf-entities) of the ezdxf query(), and the `-g`/`--groupby` option is directly in the groupby value. This will allow you to use *any* valid ezdxf properties to [groupby](https://ezdxf.readthedocs.io/en/stable/layouts/layouts.html#ezdxf.layouts.BaseLayout.groupby). The defaults are `*` for query and `color` for groupby.

## Examples

* `vpype <file> dread --groupby lineweight write lines.svg` -- This would load the file and group the layers such that each lineweight in the dxf document is a different grouped according to their lineweight.

* `vpype dread -Q 'LINE CIRCLE[color==1]' 3colors.dxf write lines-circ.svg` -- This finds and processes only the `LINE` and `CIRCLE` objects where `color==1` and writes those to the given file.

* `vpype dread -g lineweight file.dxf show --colorful` -- Will group by the lineweight and show colorful layer groupings of those groups. This can work wonders for visualizing a messy file.

* `vpype dread --groupby center circles.dxf stat` -- Will group objects by the center of their circles.

See the ezdxf documentation on query for advanced help.

https://ezdxf.readthedocs.io/en/stable/query.html

# Acknowledgement
* ezdxf author mozman did all the heavy lifting of parsing the dxf files.
* abruto's research and suggestions in issue [#5](https://github.com/tatarize/vpype-dxf/issues/5) lead to rather large increase in functionality. 

 
