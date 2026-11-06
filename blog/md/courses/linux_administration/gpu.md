# GPU Usage

* This document shows Nvdia GeForce RTX 3060 in ubuntu 24
* The HDMI was connected to NVidia RTX

## Commands

* lspci: This command lists all PCI devices, including graphics cards.
* lshw: This command provides a comprehensive list of hardware components.

```commandline
kevin@kevin-li:~$ sudo lshw -C display
  *-display                 
       description: VGA compatible controller
       product: GA106 [GeForce RTX 3060 Lite Hash Rate]
       vendor: NVIDIA Corporation
       physical id: 0
       bus info: pci@0000:01:00.0
       logical name: /dev/fb0
       version: a1
       width: 64 bits
       clock: 33MHz
       capabilities: pm msi pciexpress vga_controller bus_master cap_list rom fb
       configuration: depth=32 driver=nouveau latency=0 resolution=1920,1080
       resources: irq:132 memory:de000000-deffffff memory:c0000000-cfffffff memory:d0000000-d1ffffff ioport:e000(size=128) memory:c0000-dffff
kevin@kevin-li:~$ 
kevin@kevin-li:~$ lspci | grep -i vga
01:00.0 VGA compatible controller: NVIDIA Corporation GA106 [GeForce RTX 3060 Lite Hash Rate] (rev a1)
```

* NVIDIA-Specific Information

* OpenGL Information

`sudo apt install mesa-utils`

```commandline
kevin@kevin-li:~$ glxinfo
name of display: :1
display: :1  screen: 0
direct rendering: Yes
server glx vendor string: SGI
server glx version string: 1.4
server glx extensions:
    GLX_ARB_context_flush_control, GLX_ARB_create_context, 
    GLX_ARB_create_context_no_error, GLX_ARB_create_context_profile, 
    GLX_ARB_create_context_robustness, GLX_ARB_fbconfig_float, 
    GLX_ARB_framebuffer_sRGB, GLX_ARB_multisample, 
    GLX_EXT_create_context_es2_profile, GLX_EXT_create_context_es_profile, 
    GLX_EXT_fbconfig_packed_float, GLX_EXT_framebuffer_sRGB, 
    GLX_EXT_get_drawable_type, GLX_EXT_libglvnd, GLX_EXT_no_config_context, 
    GLX_EXT_texture_from_pixmap, GLX_EXT_visual_info, GLX_EXT_visual_rating, 
    GLX_INTEL_swap_event, GLX_MESA_copy_sub_buffer, GLX_OML_swap_method, 
    GLX_SGIS_multisample, GLX_SGIX_fbconfig, GLX_SGIX_pbuffer, 
    GLX_SGIX_visual_select_group, GLX_SGI_make_current_read, 
    GLX_SGI_swap_control
client glx vendor string: Mesa Project and SGI
client glx version string: 1.4
client glx extensions:
    GLX_ARB_context_flush_control, GLX_ARB_create_context, 
    GLX_ARB_create_context_no_error, GLX_ARB_create_context_profile, 
    GLX_ARB_create_context_robustness, GLX_ARB_fbconfig_float, 
    GLX_ARB_framebuffer_sRGB, GLX_ARB_get_proc_address, GLX_ARB_multisample, 
    GLX_ATI_pixel_format_float, GLX_EXT_buffer_age, 
    GLX_EXT_create_context_es2_profile, GLX_EXT_create_context_es_profile, 
    GLX_EXT_fbconfig_packed_float, GLX_EXT_framebuffer_sRGB, 
    GLX_EXT_import_context, GLX_EXT_no_config_context, GLX_EXT_swap_control, 
    GLX_EXT_swap_control_tear, GLX_EXT_texture_from_pixmap, 
    GLX_EXT_visual_info, GLX_EXT_visual_rating, GLX_INTEL_swap_event, 
    GLX_MESA_copy_sub_buffer, GLX_MESA_gl_interop, GLX_MESA_query_renderer, 
    GLX_MESA_swap_control, GLX_NV_float_buffer, GLX_OML_sync_control, 
    GLX_SGIS_multisample, GLX_SGIX_fbconfig, GLX_SGIX_pbuffer, 
    GLX_SGIX_visual_select_group, GLX_SGI_make_current_read, 
    GLX_SGI_swap_control, GLX_SGI_video_sync
GLX version: 1.4
GLX extensions:
    GLX_ARB_context_flush_control, GLX_ARB_create_context, 
    GLX_ARB_create_context_no_error, GLX_ARB_create_context_profile, 
    GLX_ARB_create_context_robustness, GLX_ARB_fbconfig_float, 
    GLX_ARB_framebuffer_sRGB, GLX_ARB_get_proc_address, GLX_ARB_multisample, 
    GLX_EXT_buffer_age, GLX_EXT_create_context_es2_profile, 
    GLX_EXT_create_context_es_profile, GLX_EXT_fbconfig_packed_float, 
    GLX_EXT_framebuffer_sRGB, GLX_EXT_no_config_context, GLX_EXT_swap_control, 
    GLX_EXT_swap_control_tear, GLX_EXT_texture_from_pixmap, 
    GLX_EXT_visual_info, GLX_EXT_visual_rating, GLX_INTEL_swap_event, 
    GLX_MESA_copy_sub_buffer, GLX_MESA_gl_interop, GLX_MESA_query_renderer, 
    GLX_MESA_swap_control, GLX_OML_sync_control, GLX_SGIS_multisample, 
    GLX_SGIX_fbconfig, GLX_SGIX_pbuffer, GLX_SGIX_visual_select_group, 
    GLX_SGI_make_current_read, GLX_SGI_swap_control, GLX_SGI_video_sync
Extended renderer info (GLX_MESA_query_renderer):
    Vendor: Mesa (0x10de)
    Device: NV176 (0x2504)
    Version: 24.0.9
    Accelerated: yes
    Video memory: 12267MB
    Unified memory: no
    Preferred profile: core (0x1)
    Max core profile version: 4.3
    Max compat profile version: 4.3
    Max GLES1 profile version: 1.1
    Max GLES[23] profile version: 3.2
Memory info (GL_ATI_meminfo):
    VBO free memory - total: 9814 MB, largest block: 9814 MB
    VBO free aux. memory - total: 1677721 MB, largest block: 1677721 MB
    Texture free memory - total: 9814 MB, largest block: 9814 MB
    Texture free aux. memory - total: 1677721 MB, largest block: 1677721 MB
    Renderbuffer free memory - total: 9814 MB, largest block: 9814 MB
    Renderbuffer free aux. memory - total: 1677721 MB, largest block: 1677721 MB
Memory info (GL_NVX_gpu_memory_info):
    Dedicated video memory: 12267 MB
    Total available memory: 12267 MB
    Currently available dedicated video memory: 9814 MB
OpenGL vendor string: Mesa
OpenGL renderer string: NV176
OpenGL core profile version string: 4.3 (Core Profile) Mesa 24.0.9-0ubuntu0.3
OpenGL core profile shading language version string: 4.30
OpenGL core profile context flags: (none)
OpenGL core profile profile mask: core profile
OpenGL core profile extensions:
    GL_AMD_conservative_depth, GL_AMD_draw_buffers_blend, 
    GL_AMD_gpu_shader_int64, GL_AMD_multi_draw_indirect, 
    GL_AMD_query_buffer_object, GL_AMD_seamless_cubemap_per_texture, 
    GL_AMD_shader_trinary_minmax, GL_AMD_texture_texture4, 
    GL_AMD_vertex_shader_layer, GL_AMD_vertex_shader_viewport_index, 
    GL_ANGLE_texture_compression_dxt3, GL_ANGLE_texture_compression_dxt5, 
    ....

OpenGL version string: 4.3 (Compatibility Profile) Mesa 24.0.9-0ubuntu0.3
OpenGL shading language version string: 4.30
OpenGL context flags: (none)
OpenGL profile mask: compatibility profile
OpenGL extensions:
    GL_AMD_conservative_depth, GL_AMD_draw_buffers_blend, 
    GL_AMD_multi_draw_indirect, GL_AMD_query_buffer_object, 
    GL_AMD_seamless_cubemap_per_texture, GL_AMD_shader_trinary_minmax, 
    GL_AMD_texture_texture4, GL_AMD_vertex_shader_layer, 
    GL_AMD_vertex_shader_viewport_index, GL_ANGLE_texture_compression_dxt3, 
    GL_ANGLE_texture_compression_dxt5, GL_APPLE_packed_pixels, 
    GL_ARB_ES2_compatibility, GL_ARB_ES3_1_compatibility, 
    GL_ARB_ES3_2_compatibility, GL_ARB_ES3_compatibility, 
    .....
```

### Other Graphics Viewer Tools

* vulkaninfo

`sudo apt install vulkan-tools`

```commandline
kevin@kevin-li:~$ vulkaninfo
WARNING: [Loader Message] Code 0 : terminator_CreateInstance: Failed to CreateInstance in ICD 2.  Skipping ICD.
==========
VULKANINFO
==========

Vulkan Instance Version: 1.3.204


Instance Extensions: count = 20
===============================
	VK_EXT_acquire_drm_display             : extension revision 1
	VK_EXT_acquire_xlib_display            : extension revision 1
	VK_EXT_debug_report                    : extension revision 10
	VK_EXT_debug_utils                     : extension revision 2
	VK_EXT_direct_mode_display             : extension revision 1
	VK_EXT_display_surface_counter         : extension revision 1
	VK_EXT_swapchain_colorspace            : extension revision 4
	VK_KHR_device_group_creation           : extension revision 1
	VK_KHR_display                         : extension revision 23
	VK_KHR_external_fence_capabilities     : extension revision 1
...
```

* clinfo

`sudo apt install clinfo`

```commandline
kevin@kevin-li:~$ clinfo
Number of platforms                               0

ICD loader properties
  ICD loader Name                                 OpenCL ICD Loader
  ICD loader Vendor                               OCL Icd free software
  ICD loader Version                              2.3.2
  ICD loader Profile                              OpenCL 3.0
```
