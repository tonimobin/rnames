import pandas as pd

def binning_outputs_equal(a, b):
    fa = pd.read_csv(a)
    fb = pd.read_csv(b)
    cols = list(fa.columns.values)

    def sort_refs(row):
        row = row.split(", ")
        row = map(int, row)
        row = sorted(row)
        row = map(str, row)
        concatenator = ', '
        return concatenator.join(row)
    fa.loc[:,'refs'] = fa['refs'].apply(sort_refs)
    fb.loc[:, 'refs'] = fb['refs'].apply(sort_refs)
    fa.sort_values(by=cols, inplace=True)
    fb.sort_values(by=cols, inplace=True)

    df = fa.merge(fb, how='outer', indicator=True)
    only2 = df[df['_merge'] == 'right_only']
    if len(only2) > 0:
        print(a)
        print(only2)

    pd.testing.assert_frame_equal(fa, fb)