from __future__ import division
import numpy as np
import pyopencl as cl
import pyopencl.array
#%%
%load_ext pyopencl.ipython_ext
#%%
ctx = cl.create_some_context(interactive=True)
queue = cl.CommandQueue(ctx)
#%%
%%cl_kernel -o "-cl-fast-relaxed-math"

__kernel void sum_vector(__global const float *a,
__global const float *b, __global float *c)
{
  int gid = get_global_id(0);
  c[gid] = a[gid] + b[gid];
}
#%%
n = 10000

a = cl.array.empty(queue, n, dtype=np.float32)
a.fill(15)

b_host = np.random.randn(n).astype(np.float32)
b = cl.array.to_device(queue, b_host)

c = cl.array.empty_like(a)
#%%
sum_vector(queue, (n,), None, a.data, b.data, c.data)
#%%
assert (c.get() == b_host + 15).all()