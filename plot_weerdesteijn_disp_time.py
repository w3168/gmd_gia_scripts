import matplotlib.pyplot as plt
import matplotlib


import pandas as pd
import numpy as np

#displacement = pd.read_csv("displacement_vom_arrays.csv")
#disp_2 = pd.read_csv("to200km_nz40scaled_a4.0_dt2years_dtout25years_Tend200years_extruded_tanh_iceload/displacement_vom_arrays.csv")

surface_dx = 1000
distance_fromcentre = []
n = round(1500e3 / surface_dx)

for i in range(n):
    r = np.sqrt(2*(i*surface_dx)**2)
    distance_fromcentre.append(r)
distance_fromcentre = np.array(distance_fromcentre)
print(r)

print(np.where(distance_fromcentre<100000))
print(distance_fromcentre[70])
print(distance_fromcentre[71])


def plot_time(filename, dt=50, start=0):

     
    displacement_array = pd.read_csv(filename)
    print("len array", len(displacement_array["displacement_vom_array_100years"]))
    index = np.argmin(displacement_array["displacement_vom_array_100years"])
    displacement_array = displacement_array.to_numpy()
    
    time_array = [start + i*dt for i in range(len(displacement_array[0,1:]))]

    return time_array, displacement_array, index


displacement = pd.read_csv("/data/free_surface/aspect_box/11.10.23_208cores_viscoelastic_weerdesteijn_aspectbox_dx5kmto200km_nz160scaled_a4.0_dt2years_dtout25years_Tend200years_extruded_tanh_iceload/displacement_vom_arrays.csv")

displacement_40 = pd.read_csv("/data/free_surface/aspect_box/11.10.23_208cores_testout_inputorder_newFD_redundant_viscoelastic_weerdesteijn_aspectbox_dx5kmto200km_nz40scaled_a4.0_dt2years_dtout25years_Tend200years_extruded_tanh_iceload/displacement_vom_arrays.csv")

displacement_rhog = pd.read_csv("/data/free_surface/aspect_box/12.10.23_208cores_viscoelastic_weerdesteijn_aspectbox_dx5kmto200km_nz40scaled_a4.0_dt2years_dtout25years_Tend200years_extruded_tanh_iceload_drhogice/displacement_vom_arrays.csv")

displacement_zhong = pd.read_csv("/data/free_surface/aspect_box/12.10.23_208cores_viscoelastic_weerdesteijn_aspectbox_dx5kmto200km_nz40scaled_a4.0_dt2years_dtout25years_Tend200years_extruded_tanh_iceload_drhogice_zhongprefactor/displacement_vom_arrays.csv")

displacement_zhong_topid = pd.read_csv("/data/free_surface/aspect_box/13.10.23_208cores_viscoelastic_weerdesteijn_aspectbox_dx5kmto200km_nz40scaled_a4.0_dt2years_dtout25years_Tend200years_extruded_tanh_iceload_drhogice_zhongprefactor_freesurfacetop/displacement_vom_arrays.csv")

displacement_zhong_topid_prestress = pd.read_csv("/data/free_surface/aspect_box/13.10.23_208cores_viscoelastic_weerdesteijn_aspectbox_dx5kmto200km_nz40scaled_a4.0_dt2years_dtout25years_Tend200years_extruded_tanh_iceload_drhogice_zhongprefactor_freesurfacetop_hydprestressinprevstress/displacement_vom_arrays.csv")
displacement_zhong_topid_prestress_pos = pd.read_csv("/data/free_surface/aspect_box/13.10.23_208cores_viscoelastic_weerdesteijn_aspectbox_dx5kmto200km_nz40scaled_a4.0_dt2years_dtout25years_Tend200years_extruded_tanh_iceload_drhogice_zhongprefactor_freesurfacetop_hydprestressinprevstress_pos/displacement_vom_arrays.csv")

displacement_zhong_topid_prestress_pos_nodrhog = pd.read_csv("/data/free_surface/aspect_box/13.10.23_208cores_viscoelastic_weerdesteijn_aspectbox_dx5kmto200km_nz40scaled_a4.0_dt2years_dtout25years_Tend200years_extruded_tanh_drhogice_zhongprefactor_freesurfacetop_hydprestressinprevstress_pos_withouticeloadadv/displacement_vom_arrays.csv")
displacement_zhong_topid_prestress_pos_nodrhog_80 = pd.read_csv("/data/free_surface/aspect_box/13.10.23_208cores_viscoelastic_weerdesteijn_aspectbox_dx5kmto200km_nz80scaled_a4.0_dt2years_dtout25years_Tend200years_extruded_tanh_drhogice_zhongprefactor_freesurfacetop_hydprestressinprevstress_pos_withouticeloadadv/displacement_vom_arrays.csv")
displacement_zhong_topid_prestress_pos_nodrhog_160 = pd.read_csv("/data/free_surface/aspect_box/13.10.23_208cores_viscoelastic_weerdesteijn_aspectbox_dx5kmto200km_nz160scaled_a4.0_dt2years_dtout25years_Tend200years_extruded_tanh_drhogice_zhongprefactor_freesurfacetop_hydprestressinprevstress_pos_withouticeloadadv/displacement_vom_arrays.csv")


displacement_zhong_topid_nodrhog = pd.read_csv("/data/free_surface/aspect_box/14.10.23_208cores_viscoelastic_weerdesteijn_aspectbox_dx5kmto200km_nz40scaled_a4.0_dt2years_dtout25years_Tend200years_extruded_tanh_zhongprefactor/displacement_vom_arrays.csv")
displacement_zhong_topid_nodrhog_80 = pd.read_csv("/data/free_surface/aspect_box/14.10.23_208cores_viscoelastic_weerdesteijn_aspectbox_dx5kmto200km_nz80scaled_a4.0_dt2years_dtout25years_Tend200years_extruded_tanh_zhongprefactor/displacement_vom_arrays.csv")


# old firedrake with surface advection on! this seems to be the best so far!!
disp_oldFD_surfadv = np.loadtxt("16.10.23_oldFD_40layers_surfadv_on.csv", delimiter=',')


disp_oldFD_surfadv_80 = pd.read_csv("/data/free_surface/aspect_box/16.10.23_208cores_viscoelastic_weerdesteijn_aspectbox_dx5kmto200km_nz80scaled_a4.0_dt2years_dtout25years_Tend200years_extruded_tanh_zhongprefactor_oldFD_advsurfon_oldvom/displacement_oldvom_arrays.csv")

print("old fd 80 layers")
print(np.sort(disp_oldFD_surfadv_80["displacement_vom_array_200years"]))
print(np.argmin(disp_oldFD_surfadv_80["displacement_vom_array_200years"]))
index = np.argmin(disp_oldFD_surfadv_80["displacement_vom_array_200years"])
print("index argmax = ", disp_oldFD_surfadv_80["displacement_vom_array_200years"][index] )

print()

disp_oldFD_surfadv_80_check = pd.read_csv("/data/free_surface/aspect_box/18.10.23_208cores_viscoelastic_weerdesteijn_aspectbox_dx5kmto200km_nz80scaled_a4.0_dt2years_dtout10years_Tend200years_extruded_zhongprefactor_oldFD_checkpoint/displacement_oldvom_arrays.csv")

index_check = np.argmin(disp_oldFD_surfadv_80_check["displacement_vom_array_200years"])

disp_oldFD_long = pd.read_csv("/data/free_surface/aspect_box/17.10.23_208cores_viscoelastic_weerdesteijn_aspectbox_dx5kmto200km_nz80scaled_a4.0_dt50years_dtout315576000000.025years_Tend3471336000000.0years_extruded_tanh_zhongprefactor_oldFD_advsurfon_oldvom/displacement_oldvom_arrays.csv")

disp_oldFD_long = pd.read_csv("/data/free_surface/aspect_box/18.10.23_208cores_viscoelastic_weerdesteijn_aspectbox_dx5kmto200km_nz80scaled_a4.0_dt50years_dtout10000years_Tend110000years_extruded_zhongprefactor_oldFD_checkpoint/displacement_oldvom_arrays.csv")
print(np.sort(disp_oldFD_long["displacement_vom_array_200years"]))
print(np.argmin(disp_oldFD_long["displacement_vom_array_200years"]))
index_long = np.argmin(disp_oldFD_long["displacement_vom_array_200years"])
print("index argmax = ", disp_oldFD_long["displacement_vom_array_200years"][index_long] )

print()
disp_oldFD_long_rho1g = pd.read_csv("/data/free_surface/aspect_box/18.10.23_208cores_viscoelastic_weerdesteijn_aspectbox_dx5kmto200km_nz80scaled_a4.0_dt50years_dtout10000years_Tend110000years_extruded_zhongprefactor_oldFD_checkpoint_rho1g/displacement_oldvom_arrays.csv")
print(np.sort(disp_oldFD_long_rho1g["displacement_vom_array_200years"]))
print(np.argmin(disp_oldFD_long_rho1g["displacement_vom_array_200years"]))
index_long_rho1g = np.argmin(disp_oldFD_long_rho1g["displacement_vom_array_200years"])
print("index argmax = ", disp_oldFD_long_rho1g["displacement_vom_array_200years"][index_long_rho1g] )

print()


disp_oldFD_long_gradmesh = pd.read_csv("/data/free_surface/aspect_box/19.10.23_832cores_viscoelastic_weerdesteijn_aspectbox_dx5kmto200km_nz80scaled_a4.0_dt50years_dtout10000years_Tend110000years_extruded_zhongprefactor_oldFD_checkpoint_gradualmesh/displacement_oldvom_arrays.csv")
index_long_gradmesh = np.argmin(disp_oldFD_long_gradmesh["displacement_vom_array_200years"])

disp_oldFD_long_gradmesh_TDG2 = pd.read_csv("/data/free_surface/aspect_box/23.10.23_832cores_viscoelastic_weerdesteijn_aspectbox_dx5kmto200km_nz80scaled_a4.0_dt50years_dtout1000years_Tend110000years_extruded_zhongprefactor_oldFD_weakbcs_TDG2interp/displacement_oldvom_arrays.csv")

index_long_gradmesh_TDG2 = np.argmin(disp_oldFD_long_gradmesh_TDG2["displacement_vom_array_200years"])

disp_oldFD_long_gradmesh_TDG2_rho1g = pd.read_csv("/data/free_surface/aspect_box/25.10.23_832cores_viscoelastic_weerdesteijn_aspectbox_dx5km_nz80scaled_a4_dt50years_dtout1000years_Tend110000years_extruded_zhongprefactor_oldFD_weak_TDG2interp_rho1g/displacement_oldvom_arrays.csv")
index_long_gradmesh_TDG2_rho1g = np.argmin(disp_oldFD_long_gradmesh_TDG2_rho1g["displacement_vom_array_200years"])

disp_oldFD_long_gradmesh_TDG2_strong = pd.read_csv("/data/free_surface/aspect_box/25.10.23_832cores_viscoelastic_weerdesteijn_aspectbox_dx5km_nz80scaled_a4_dt50years_dtout1000years_Tend110000years_extruded_zhongprefactor_oldFD_TDG2interp_strong_1e10scale/displacement_oldvom_arrays.csv")
index_long_gradmesh_TDG2_strong = np.argmin(disp_oldFD_long_gradmesh_TDG2_strong["displacement_vom_array_200years"])

disp_oldFD_long_gradmesh_TDG2_from64ka = pd.read_csv("/data/free_surface/aspect_box/25.10.23_832cores4_viscoelastic_weerdesteijn_aspectbox_dx5km_nz80scaled_a4_dt50years_dtout1000years_Tend110000years_extruded_zhongprefactor_oldFD_weak_TDG2interp_from64ka/displacement_oldvom_arrays.csv")
index_long_gradmesh_TDG2_from64ka = np.argmin(disp_oldFD_long_gradmesh_TDG2_from64ka["displacement_vom_array_64050years"])

disp_oldFD_long_gradmesh_TDG2_strong_gradp = pd.read_csv("/data/free_surface/aspect_box/26.10.23_832cores_viscoelastic_weerdesteijn_aspectbox_dx5km_nz80scaled_a4_dt50years_dtout1000years_Tend110000years_extruded_zhongprefactor_oldFD_TDG2interp_strong_1e10scale_pres/displacement_oldvom_arrays.csv")
index_long_gradmesh_TDG2_strong_gradp = np.argmin(disp_oldFD_long_gradmesh_TDG2_strong_gradp["displacement_vom_array_200years"])


disp_oldFD_long_gradmesh_TDG2_weak_scale = pd.read_csv("/data/free_surface/aspect_box/26.10.23_832cores_viscoelastic_weerdesteijn_aspectbox_dx5km_nz80scaled_a4_dt50years_dtout1000years_Tend2000years_extruded_zhongprefactor_oldFD_TDG2interp_weak_1e10scale_pres/displacement_oldvom_arrays.csv")
index_long_gradmesh_TDG2_weak_scale = np.argmin(disp_oldFD_long_gradmesh_TDG2_weak_scale["displacement_vom_array_200years"])

disp_oldFD_long_gradmesh_TDG2_from75_drhog = pd.read_csv("/data/free_surface/aspect_box/26.10.23_832cores4_viscoelastic_weerdesteijn_aspectbox_dx5km_nz80scaled_a4_dt50years_dtout1000years_Tend110000years_extruded_zhongprefactor_oldFD_weak_TDG2interp_from75ka_drhog/displacement_oldvom_arrays.csv")

disp_oldFD_long_gradmesh_TDG2_strong_scaleprevstress = pd.read_csv("/data/free_surface/aspect_box/26.10.23_832cores2_viscoelastic_weerdesteijn_aspectbox_dx5km_nz80scaled_a4_dt50years_dtout1000years_Tend110000years_extruded_zhongprefactor_oldFD_TDG2interp_strong_1e10scale_pres_prevstressvisc/displacement_oldvom_arrays.csv")
index_long_gradmesh_TDG2_strong_scaleprevstress = np.argmin(disp_oldFD_long_gradmesh_TDG2_strong_scaleprevstress["displacement_vom_array_200years"])

#disp_oldFD_long_gradmesh_TDG2_drhog = pd.read_csv("/data/free_surface/aspect_box/26.10.23_832cores_viscoelastic_weerdesteijn_aspectbox_dx5km_nz80scaled_a4_dt50years_dtout1000years_Tend110000years_extruded_zhongprefactor_oldFD_weak_TDG2interp_drhog/displacement_oldvom_arrays.csv")
disp_oldFD_long_gradmesh_TDG2_drhog = pd.read_csv("/data/free_surface/aspect_box/27.10.23_832cores_viscoelastic_weerdesteijn_aspectbox_dx5km_nz80scaled_a4_dt50years_dtout10000years_Tend110000years_extruded_zhongprefactor_oldFD_weak_TDG2interp_drhog/displacement_oldvom_arrays.csv")
index_long_gradmesh_TDG2_drhog = np.argmin(disp_oldFD_long_gradmesh_TDG2_drhog["displacement_vom_array_200years"])

disp_oldFD_long_gradmesh_TDG2_drhog_rho1g = pd.read_csv("/data/free_surface/aspect_box/27.10.23_832cores_viscoelastic_weerdesteijn_aspectbox_dx5km_nz80scaled_a4_dt50years_dtout10000years_Tend110000years_extruded_zhongprefactor_oldFD_weak_TDG2interp_drhog_rho1g/displacement_oldvom_arrays.csv")
index_long_gradmesh_TDG2_drhog_rho1g = np.argmin(disp_oldFD_long_gradmesh_TDG2_drhog_rho1g["displacement_vom_array_200years"])

disp_oldFD_long_gradmesh_TDG2_drhog_rho1g_strong = pd.read_csv("/data/free_surface/aspect_box/27.10.23_832cores_viscoelastic_weerdesteijn_aspectbox_dx5km_nz80scaled_a4_dt50years_dtout10000years_Tend110000years_extruded_zhongprefactor_oldFD_TDG2interp_strong1e10_drhorho1/displacement_oldvom_arrays.csv")
index_long_gradmesh_TDG2_drhog_rho1g_strong = np.argmin(disp_oldFD_long_gradmesh_TDG2_drhog_rho1g_strong["displacement_vom_array_200years"])

disp_oldFD_long_gradmesh_TDG2_nodrhog = pd.read_csv("/data/free_surface/aspect_box/29.10.23_832cores_viscoelastic_weerdesteijn_aspectbox_dx5km_nz80scaled_a4_dt50years_dtout10000years_Tend110000years_extruded_zhongprefactor_oldFD_weak_TDG2interp_nodrhog/displacement_oldvom_arrays.csv")

index_long_gradmesh_TDG2_nodrhog = np.argmin(disp_oldFD_long_gradmesh_TDG2_nodrhog["displacement_vom_array_200years"])

disp_oldFD_long_gradmesh_TDG2_zerodrhog_norho1 = pd.read_csv("/data/free_surface/aspect_box/06.12.23_832cores_viscoelastic_weerdesteijn_aspectbox_dx5km_nz80scaled_a4_dt50years_dtout10000years_Tend110000years_extruded_zhongprefactor_oldFD_TDG2interp_strong1e10_nodrho_norho1/displacement_oldvom_arrays.csv")
index_long_gradmesh_TDG2_zerodrhog_norho1 = np.argmin(disp_oldFD_long_gradmesh_TDG2_zerodrhog_norho1["displacement_vom_array_200years"])

disp_oldFD_long_gradmesh_TDG2_zerodrhog_rho1 = pd.read_csv("/data/free_surface/aspect_box/06.12.23_832cores_viscoelastic_weerdesteijn_aspectbox_dx5km_nz80scaled_a4_dt50years_dtout10000years_Tend110000years_extruded_zhongprefactor_oldFD_TDG2interp_strong1e10_nodrho_rho1/displacement_oldvom_arrays.csv")
index_long_gradmesh_TDG2_zerodrhog_rho1 = np.argmin(disp_oldFD_long_gradmesh_TDG2_zerodrhog_rho1["displacement_vom_array_200years"])

disp_oldFD_long_gradmesh_TDG2_drhog_rho1_move = pd.read_csv("/data/free_surface/aspect_box/06.12.23_832cores_viscoelastic_weerdesteijn_aspectbox_dx5km_nz80scaled_a4_dt50years_dtout10000years_Tend110000years_extruded_zhongprefactor_oldFD_TDG2interp_strong1e10_drhorho1_movemesh/displacement_oldvom_arrays.csv")
index_long_gradmesh_TDG2_drhog_move = np.argmin(disp_oldFD_long_gradmesh_TDG2_drhog_rho1_move["displacement_vom_array_200years"])

disp_oldFD_long_gradmesh_TDG2_rho1_bodypresadv = pd.read_csv("/data/free_surface/aspect_box/11.12.23_832cores_viscoelastic_weerdesteijn_aspectbox_dx5km_nz80scaled_a4_dt50years_dtout10000years_Tend110000years_extruded_zhongprefactor_oldFD_TDG2interp_strong1e10_rho1_bodypresadv/displacement_oldvom_arrays.csv")
index_long_gradmesh_TDG2_rho1_bodypresadv = np.argmin(disp_oldFD_long_gradmesh_TDG2_rho1_bodypresadv["displacement_vom_array_200years"])


disp_oldFD_long_gradmesh_TDG2_drhog_lagrbuoy = pd.read_csv("/data/free_surface/aspect_box/12.12.23_832cores_viscoelastic_weerdesteijn_aspectbox_dx5km_nz80scaled_a4_dt50years_dtout10000years_Tend110000years_extruded_zhongprefactor_oldFD_TDG2interp_strong1e10_drho_lagrbuoy_movemesh/displacement_oldvom_arrays.csv")
index_long_gradmesh_TDG2_drhog_lagrbuoy = np.argmin(disp_oldFD_long_gradmesh_TDG2_drhog_lagrbuoy["displacement_vom_array_200years"])

disp_oldFD_long_gradmesh_TDG2_drhog_norho1_move = pd.read_csv("/data/free_surface/aspect_box/12.12.23_832cores_viscoelastic_weerdesteijn_aspectbox_dx5km_nz80scaled_a4_dt50years_dtout10000years_Tend110000years_extruded_zhongprefactor_oldFD_TDG2interp_strong1e10_drho_norho1_movemesh/displacement_oldvom_arrays.csv")

index_long_gradmesh_TDG2_drhog_norho1_move = np.argmin(disp_oldFD_long_gradmesh_TDG2_drhog_norho1_move["displacement_vom_array_200years"])

disp_oldFD_long_gradmesh_TDG2_drhog_advrho1 = pd.read_csv("/data/free_surface/aspect_box/18.12.23_832cores_viscoelastic_weerdesteijn_aspectbox_dx5km_nz80scaled_a4_dt50years_dtout10000years_Tend110000years_extruded_zhongprefactor_oldFD_TDG2interp_strong1e10_drhorho1_advectrho/displacement_oldvom_arrays.csv")
index_long_gradmesh_TDG2_drhog_advrho1 = np.argmin(disp_oldFD_long_gradmesh_TDG2_drhog_advrho1["displacement_vom_array_200years"])

disp_oldFD_long_gradmesh_TDG2_drhog_advrho1_move = pd.read_csv("/data/free_surface/aspect_box/18.12.23_832cores_viscoelastic_weerdesteijn_aspectbox_dx5km_nz80scaled_a4_dt50years_dtout10000years_Tend110000years_extruded_zhongprefactor_oldFD_TDG2interp_strong1e10_drho_lagrbuoy_movemesh_advect/displacement_oldvom_arrays.csv")
index_long_gradmesh_TDG2_drhog_advrho1_move = np.argmin(disp_oldFD_long_gradmesh_TDG2_drhog_advrho1_move["displacement_vom_array_200years"])


disp_oldFD_long_gradmesh_TDG2_rhog_dump75 = pd.read_csv("/data/free_surface/aspect_box/21.12.23_832cores_viscoelastic_weerdesteijn_aspectbox_dx5km_nz80scaled_a4_dt50years_dtout10000years_Tend110000years_extruded_zhongprefactor_oldFD_weak_TDG2interp_from75ka/displacement_oldvom_arrays.csv")
index_long_gradmesh_TDG2_rhog_dump75 = np.argmin(disp_oldFD_long_gradmesh_TDG2_rhog_dump75["displacement_vom_array_75050years"])

disp_oldFD_long_gradmesh_TDG2_rhog_110ka = pd.read_csv("/data/free_surface/aspect_box/22.12.23_832cores_viscoelastic_weerdesteijn_aspectbox_dx5km_nz80scaled_a4_dt50years_dtout10000years_Tend110000years_extruded_zhongprefactor_oldFD_weak_TDG2interp_rhog_rho1_from110ka/displacement_oldvom_arrays.csv")
index_long_gradmesh_TDG2_rhog_110ka = np.argmin(disp_oldFD_long_gradmesh_TDG2_rhog_110ka["displacement_vom_array_110050years"])


#disp_oldFD_long_gradmesh_TDG2_drhog_110ka = pd.read_csv("/data/free_surface/aspect_box/22.12.23_832cores_viscoelastic_weerdesteijn_aspectbox_dx5km_nz80scaled_a4_dt50years_dtout50000years_Tend110000years_extruded_zhongprefactor_oldFD_TDG2interp_strong1e10_drhorho1_from110ka/displacement_oldvom_arrays.csv")
disp_oldFD_long_gradmesh_TDG2_drhog_110ka = pd.read_csv("/data/free_surface/aspect_box/04.01.24_832cores_viscoelastic_weerdesteijn_aspectbox_dx5km_nz80scaled_a4_dt50years_dtout50000years_Tend110000years_extruded_zhongprefactor_oldFD_TDG2interp_strong1e10_drhorho1_from110kafixscalemu/displacement_oldvom_arrays.csv")

disp_oldFD_long_gradmesh_TDG2_drhog_isostatic = pd.read_csv("/data/free_surface/aspect_box/22.12.23_832cores_viscoelastic_weerdesteijn_aspectbox_dx5km_nz80scaled_a4_dt50years_dtout25000years_Tend330000years_extruded_zhongprefactor_oldFD_TDG2interp_strong1e10_drhorho1_isostatic/displacement_oldvom_arrays.csv")
index_long_gradmesh_TDG2_drhog_iso = np.argmin(disp_oldFD_long_gradmesh_TDG2_drhog_isostatic["displacement_vom_array_100years"])

disp_oldFD_long_gradmesh_TDG2_rhog_isostatic = pd.read_csv("/data/free_surface/aspect_box/22.12.23_832cores_viscoelastic_weerdesteijn_aspectbox_dx5km_nz80scaled_a4_dt50years_dtout25000years_Tend330000years_extruded_zhongprefactor_oldFD_TDG2interp_strong1e10_rhorho1_isostatic/displacement_oldvom_arrays.csv")
index_long_gradmesh_TDG2_rhog_iso = np.argmin(disp_oldFD_long_gradmesh_TDG2_rhog_isostatic["displacement_vom_array_100years"])


disp_oldFD_long_gradmesh_TDG2_drhog_isostatic_nolith = pd.read_csv("/data/free_surface/aspect_box/09.01.23_832cores_viscoelastic_weerdesteijn_aspectbox_dx5km_nz80scaled_a4_dt50years_dtout25000years_Tend330000years_extruded_zhongprefactor_oldFD_TDG2interp_strong1e10_drhorho1_isostatic_nolith/displacement_oldvom_arrays.csv")
index_long_gradmesh_TDG2_drhog_iso_nolith = np.argmin(disp_oldFD_long_gradmesh_TDG2_drhog_isostatic_nolith["displacement_vom_array_100years"])

disp_oldFD_long_gradmesh_TDG2_rhog_isostatic_nolith = pd.read_csv("/data/free_surface/aspect_box/09.01.23_832cores_viscoelastic_weerdesteijn_aspectbox_dx5km_nz80scaled_a4_dt50years_dtout25000years_Tend330000years_extruded_zhongprefactor_oldFD_TDG2interp_strong1e10_rhorho1_isostatic_nolith/displacement_oldvom_arrays.csv")
index_long_gradmesh_TDG2_rhog_iso_nolith = np.argmin(disp_oldFD_long_gradmesh_TDG2_rhog_isostatic_nolith["displacement_vom_array_100years"])

#disp_oldFD_long_gradmesh_TDG2_rhog_isostatic_nolith_func = plot_time("/data/free_surface/aspect_box/09.01.23_832cores_viscoelastic_weerdesteijn_aspectbox_dx5km_nz80scaled_a4_dt50years_dtout25000years_Tend330000years_extruded_zhongprefactor_oldFD_TDG2interp_strong1e10_rhorho1_isostatic_nolith/displacement_oldvom_arrays.csv")


#disp_drhog_iso_nolith_func = plot_time("/data/free_surface/aspect_box/09.01.23_832cores_viscoelastic_weerdesteijn_aspectbox_dx5km_nz80scaled_a4_dt50years_dtout25000years_Tend330000years_extruded_zhongprefactor_oldFD_TDG2interp_strong1e10_drhorho1_isostatic_nolith/displacement_oldvom_arrays.csv")


#disp_TP1 = plot_time("/data/free_surface/aspect_box/24.01.24_832cores_viscoelastic_weerdesteijn_aspectbox_dx5km_nz80scaled_a4_dt50years_dtout50000years_Tend110000years_extruded_zhongprefactor_oldFD_TDG2interp_strong1e10_drhorho1_TP1/displacement_oldvom_arrays.csv")


print("old gadi")
disp_2d_old = plot_time("/data/viscoelastic/2d_aspect_box/19.02.24_16cores_2d_viscoelastic_weerdesteijn_aspectbox_dx5km_nz80scaled_a4_dt50years_dtout50000years_Tend110000years_extruded_zhongprefactor_oldFD_TDG2interp_strong1e10_drhorho1/displacement_oldvom_arrays.csv")

#disp_2d_new = plot_time("/data/viscoelastic/2d_aspect_box/20.02.24_2d_new_viscoelastic_weerdesteijn_aspectbox_dx5km_nz80scaled_a4_dt50years_dtout50000years_Tend110000years_minusiceload_exteriordens/displacement_oldvom_arrays.csv")
#disp_2d_new_zerodens = plot_time("/data/viscoelastic/2d_aspect_box/20.02.24_2d_new_viscoelastic_weerdesteijn_aspectbox_dx5km_nz80scaled_a4_dt50years_dtout50000years_Tend110000years_minusiceload_exteriordenszero/displacement_oldvom_arrays.csv")
#disp_2d_new_fs = plot_time("/data/viscoelastic/2d_aspect_box/20.02.24_2d_new_viscoelastic_weerdesteijn_aspectbox_dx5km_nz80scaled_a4_dt50years_dtout50000years_Tend110000years_minusiceload_tryfs/displacement_oldvom_arrays.csv")
#disp_2d_new_fs_exd = plot_time("/data/viscoelastic/2d_aspect_box/20.02.24_2d_new_viscoelastic_weerdesteijn_aspectbox_dx5km_nz80scaled_a4_dt50years_dtout50000years_Tend110000years_minusiceload_tryfs_exteriordensity/displacement_oldvom_arrays.csv")
#disp_2d_new_nofs_check = plot_time("/data/viscoelastic/2d_aspect_box/20.02.24_2d_new_viscoelastic_weerdesteijn_aspectbox_dx5km_nz80scaled_a4_dt50years_dtout50000years_Tend110000years_minusiceload_checknofs/displacement_oldvom_arrays.csv")
#disp_2d_new_check_rho1 = plot_time("/data/viscoelastic/2d_aspect_box/20.02.24_2d_new_viscoelastic_weerdesteijn_aspectbox_dx5km_nz80scaled_a4_dt50years_dtout50000years_Tend110000years_minusiceload_checkrho1/displacement_oldvom_arrays.csv")

#disp_2d_old_newFD = plot_time("/data/viscoelastic/2d_aspect_box/20.02.24_2d_viscoelastic_weerdesteijn_aspectbox_dx5km_nz80scaled_a4_dt50years_dtout50000years_Tend110000years_extruded_zhongprefactor_oldFD_TDG2interp_strong1e10_drhorho1_old/displacement_oldvom_arrays.csv")

#disp_2d_new_refnormalstress = plot_time("/data/viscoelastic/2d_aspect_box/20.02.24_2d_new_viscoelastic_weerdesteijn_aspectbox_dx5km_nz80scaled_a4_dt50years_dtout50000years_Tend110000years_minusiceload_refnormalstress/displacement_oldvom_arrays.csv")

#disp_2d_old_newFD_nofs = plot_time("/data/viscoelastic/2d_aspect_box/20.02.24_2d_viscoelastic_weerdesteijn_aspectbox_dx5km_nz80scaled_a4_dt50years_dtout50000years_Tend110000years_extruded_zhongprefactor_oldFD_TDG2interp_strong1e10_drhorho1_old_nofs/displacement_oldvom_arrays.csv")

#disp_2d_new_noF = plot_time("/data/viscoelastic/2d_aspect_box/20.02.24_2d_new_viscoelastic_weerdesteijn_aspectbox_dx5km_nz80scaled_a4_dt50years_dtout50000years_Tend110000years_minusiceload_noF/displacement_oldvom_arrays.csv")

#disp_2d_new_noprevstress = plot_time("/data/viscoelastic/2d_aspect_box/20.02.24_2d_new_viscoelastic_weerdesteijn_aspectbox_dx5km_nz80scaled_a4_dt50years_dtout50000years_Tend110000years_minusiceload_noprevstress/displacement_oldvom_arrays.csv")
print("new FD \n ")
disp_2d_new_testing = plot_time("/data/viscoelastic/2d_aspect_box/21.02.24_2d_new_viscoelastic_weerdesteijn_aspectbox_dx5km_nz80scaled_a4_dt50years_dtout1000years_Tend110000years_minusiceload_testing/displacement_oldvom_arrays.csv")
print("")
print("old visco, new FD")
disp_2d_old_newFD_testing = plot_time("/data/viscoelastic/2d_aspect_box/21.02.24_2d_viscoelastic_weerdesteijn_aspectbox_dx5km_nz80scaled_a4_dt50years_dtout1000years_Tend110000years_extruded_zhongprefactor_oldFD_TDG2interp_strong1e10_drhorho1_old_testing/displacement_oldvom_arrays.csv")

print("new FD positive ice load \n ")
disp_2d_new_testing_posice = plot_time("/data/viscoelastic/2d_aspect_box/21.02.24_2d_new_viscoelastic_weerdesteijn_aspectbox_dx5km_nz80scaled_a4_dt50years_dtout1000years_Tend110000years_posiceload_testing/displacement_oldvom_arrays.csv")


disp_2d_new_MPInodes = np.loadtxt("/data/viscoelastic/2d_aspect_box/21.02.24_2d_new_viscoelastic_weerdesteijn_aspectbox_dx5km_nz80scaled_a4_dt50years_dtout10000years_Tend110000years_posiceload_testing_dispmin/min_displacement.txt")

disp_2d_new_MPInodes_checktidy = np.loadtxt("/data/viscoelastic/2d_aspect_box/23.02.24_2d_new_viscoelastic_weerdesteijn_aspectbox_dx5km_nz80scaled_a4_dt50years_dtout10000years_Tend110000years_posiceload_testing_dispmin_tidy/min_displacement.txt")

#disp_2d_new_MPInodes_cylinderchanges = np.loadtxt("/home/wscott/g-adopt/demos/viscoelastic/displacement-testcylinderchanges-weerdesteijn-2d.dat")

#disp_2d_new_MPInodes_cylinderchanges_180324 = np.loadtxt("/home/wscott/g-adopt/demos/viscoelastic/18.03.24_displacement-testcylinderchanges-weerdesteijn-2d.dat")
#disp_2d_new_MPInodes_180324old = np.loadtxt("/home/wscott/g-adopt/demos/viscoelastic/displacement-weerdesteijn-2d.dat")
#disp_2d_new_MPInodes_180324old_meshres = np.loadtxt("/home/wscott/g-adopt/demos/viscoelastic/18.03.24_displacement-weerdesteijn-2d-meshres.dat")
##disp_2d_new_MPInodes_180324old_meshresdisc5000 = np.loadtxt("/home/wscott/g-adopt/demos/viscoelastic/displacement-weerdesteijn-2d-disc5000.dat")
#disp_2d_new_MPInodes_190324newdisc5000 = np.loadtxt("/home/wscott/g-adopt/demos/viscoelastic/displacement-testcylinderchanges-weerdesteijn-2d-newdisc5000.dat")

# 2d vertical resolution testing conditional vs tanh depth profiles

#disp_2d_nz40_conditional = np.loadtxt("/home/wscott/g-adopt/demos/viscoelastic/displacement-weerdesteijn-2d-nz40.dat")
#disp_2d_nz80_conditional = np.loadtxt("/home/wscott/g-adopt/demos/viscoelastic/displacement-weerdesteijn-2d.dat")
#disp_2d_nz160_conditional = np.loadtxt("/home/wscott/g-adopt/demos/viscoelastic/displacement-weerdesteijn-2d-nz160.dat")
#disp_2d_nz320_conditional = np.loadtxt("/home/wscott/g-adopt/demos/viscoelastic/displacement-weerdesteijn-2d-nz320.dat")
#
#disp_2d_nz40_tanh = np.loadtxt("/home/wscott/g-adopt/demos/viscoelastic/displacement-weerdesteijn-2d-nz40-tanhvert.dat")
#disp_2d_nz80_tanh = np.loadtxt("/home/wscott/g-adopt/demos/viscoelastic/displacement-weerdesteijn-2d-nz80-tanhvert.dat")
#disp_2d_nz160_tanh = np.loadtxt("/home/wscott/g-adopt/demos/viscoelastic/displacement-weerdesteijn-2d-nz160-tanhvert.dat")

#disp_2d_nz40_tanh_5km = np.loadtxt("/home/wscott/g-adopt/demos/viscoelastic/displacement-weerdesteijn-2d-nz40-tanhvert-tanh5km.dat")
#disp_2d_nz80_tanh_5km = np.loadtxt("/home/wscott/g-adopt/demos/viscoelastic/displacement-weerdesteijn-2d-nz80-tanhvert-tanh5km.dat")
#disp_2d_nz160_tanh_5km = np.loadtxt("/home/wscott/g-adopt/demos/viscoelastic/displacement-weerdesteijn-2d-nz160-tanhvert-tanh5km.dat")

#disp_2d_nz40_tanh_2pt5km = np.loadtxt("/home/wscott/g-adopt/demos/viscoelastic/displacement-weerdesteijn-2d-nz40-tanhvert-tanh2.5km.dat")
#disp_2d_nz80_tanh_2pt5km = np.loadtxt("/home/wscott/g-adopt/demos/viscoelastic/displacement-weerdesteijn-2d-nz80-tanhvert-tanh2.5km.dat")
#disp_2d_nz160_tanh_2pt5km = np.loadtxt("/home/wscott/g-adopt/demos/viscoelastic/displacement-weerdesteijn-2d-nz160-tanhvert-tanh2.5km.dat")
#disp_2d_nz320_tanh_2pt5km = np.loadtxt("/home/wscott/g-adopt/demos/viscoelastic/displacement-weerdesteijn-2d-nz320-tanhvert-tanh2.5km.dat")

#disp_2d_nz40_tanh_1km = np.loadtxt("/home/wscott/g-adopt/demos/viscoelastic/displacement-weerdesteijn-2d-nz40-tanhvert-tanh1km.dat")
#disp_2d_nz80_tanh_1km = np.loadtxt("/home/wscott/g-adopt/demos/viscoelastic/displacement-weerdesteijn-2d-nz80-tanhvert-tanh1km.dat")
#disp_2d_nz160_tanh_1km = np.loadtxt("/home/wscott/g-adopt/demos/viscoelastic/displacement-weerdesteijn-2d-nz160-tanhvert-tanh1km.dat")
#disp_2d_nz320_tanh_1km = np.loadtxt("/home/wscott/g-adopt/demos/viscoelastic/displacement-weerdesteijn-2d-nz320-tanhvert-tanh1km.dat")

#disp_2d_nz40_tanh_500m = np.loadtxt("/home/wscott/g-adopt/demos/viscoelastic/displacement-weerdesteijn-2d-nz40-tanhvert-tanh500m.dat")
#disp_2d_nz80_tanh_500m = np.loadtxt("/home/wscott/g-adopt/demos/viscoelastic/displacement-weerdesteijn-2d-nz80-tanhvert-tanh500m.dat")
#disp_2d_nz160_tanh_500m = np.loadtxt("/home/wscott/g-adopt/demos/viscoelastic/displacement-weerdesteijn-2d-nz160-tanhvert-tanh500m.dat")
#disp_2d_nz320_tanh_500m = np.loadtxt("/home/wscott/g-adopt/demos/viscoelastic/displacement-weerdesteijn-2d-nz320-tanhvert-tanh500m.dat")
#######
# 2d variable viscosity
'''
disp_2d_instantload = np.loadtxt("/home/wscott/g-adopt/demos/viscoelastic/displacement-weerdesteijn-low-viscosity-2d-dx10km-nz80-dt50years-low-viscosityFalse.dat")
disp_2d_instantload_lowvisc = np.loadtxt("/home/wscott/g-adopt/demos/viscoelastic/displacement-weerdesteijn-low-viscosity-2d-dx10km-nz80-dt50years-low-viscosityTrue.dat")

disp_2d_instantload_dx5_nz160squash = np.loadtxt("/home/wscott/g-adopt/demos/viscoelastic/displacement-inverse-viscosity-weerdesteijn-2d_5ka_squashed-dx10km-nz80-dt50years-viscosity-inversion.dat")
disp_2d_instantload_lowvisc_dx5_nz160squash = np.loadtxt("/home/wscott/g-adopt/demos/viscoelastic/displacement-weerdesteijn-low-viscosity-2d-squashed-dx5km-nz160-dt50years-low-viscosityTrue.dat")

# optimised viscosity runs
disp_2d_instantload_optvisc_lb1emin5 = np.loadtxt("/home/wscott/g-adopt/demos/viscoelastic/displacement-weerdesteijn-instant-ice-optimised-viscosity-iteration15-dx5km-nz160-dt50years-low-viscosityFalse.dat")
disp_2d_instantload_optvisc_lb1emin4 = np.loadtxt("/home/wscott/g-adopt/demos/viscoelastic/displacement-inverse-viscosity-weerdesteijn-2d_5ka_squashed-optimised-viscosity-iteration11-dx5km-nz160-dt50years-low-viscosityFalse.dat")
disp_2d_instantload_optvisc_lb1emin5_it1 = np.loadtxt("/home/wscott/g-adopt/demos/viscoelastic/displacement-inverse-viscosity-weerdesteijn-2d_5ka_squashed_lb1e-5-optimised-viscosity-iteration1-dx5km-nz160-dt50years-low-viscosityFalse.dat")

# its lb 1e-4
disp_2d_instantload_optvisc_lb1emin4_it1 = np.loadtxt("/home/wscott/g-adopt/demos/viscoelastic/displacement-inverse-viscosity-weerdesteijn-2d_5ka_squashed-optimised-viscosity-iteration1-dx5km-nz160-dt50years-low-viscosityFalse.dat")
disp_2d_instantload_optvisc_lb1emin4_it2 = np.loadtxt("/home/wscott/g-adopt/demos/viscoelastic/displacement-inverse-viscosity-weerdesteijn-2d_5ka_squashed-optimised-viscosity-iteration2-dx5km-nz160-dt50years-low-viscosityFalse.dat")
disp_2d_instantload_optvisc_lb1emin4_it3 = np.loadtxt("/home/wscott/g-adopt/demos/viscoelastic/displacement-inverse-viscosity-weerdesteijn-2d_5ka_squashed-optimised-viscosity-iteration3-dx5km-nz160-dt50years-low-viscosityFalse.dat")
disp_2d_instantload_optvisc_lb1emin4_it4 = np.loadtxt("/home/wscott/g-adopt/demos/viscoelastic/displacement-inverse-viscosity-weerdesteijn-2d_5ka_squashed-optimised-viscosity-iteration4-dx5km-nz160-dt50years-low-viscosityFalse.dat")
disp_2d_instantload_optvisc_lb1emin4_it5 = np.loadtxt("/home/wscott/g-adopt/demos/viscoelastic/displacement-inverse-viscosity-weerdesteijn-2d_5ka_squashed-optimised-viscosity-iteration5-dx5km-nz160-dt50years-low-viscosityFalse.dat")
disp_2d_instantload_optvisc_lb1emin4_it6 = np.loadtxt("/home/wscott/g-adopt/demos/viscoelastic/displacement-inverse-viscosity-weerdesteijn-2d_5ka_squashed-optimised-viscosity-iteration6-dx5km-nz160-dt50years-low-viscosityFalse.dat")
disp_2d_instantload_optvisc_lb1emin4_it7 = np.loadtxt("/home/wscott/g-adopt/demos/viscoelastic/displacement-inverse-viscosity-weerdesteijn-2d_5ka_squashed-optimised-viscosity-iteration7-dx5km-nz160-dt50years-low-viscosityFalse.dat")
disp_2d_instantload_optvisc_lb1emin4_it8 = np.loadtxt("/home/wscott/g-adopt/demos/viscoelastic/displacement-inverse-viscosity-weerdesteijn-2d_5ka_squashed-optimised-viscosity-iteration8-dx5km-nz160-dt50years-low-viscosityFalse.dat")
disp_2d_instantload_optvisc_lb1emin4_it9 = np.loadtxt("/home/wscott/g-adopt/demos/viscoelastic/displacement-inverse-viscosity-weerdesteijn-2d_5ka_squashed-optimised-viscosity-iteration9-dx5km-nz160-dt50years-low-viscosityFalse.dat")
disp_2d_instantload_optvisc_lb1emin4_it10 = np.loadtxt("/home/wscott/g-adopt/demos/viscoelastic/displacement-inverse-viscosity-weerdesteijn-2d_5ka_squashed-optimised-viscosity-iteration10-dx5km-nz160-dt50years-low-viscosityFalse.dat")
disp_2d_instantload_optvisc_lb1emin4_it11 = np.loadtxt("/home/wscott/g-adopt/demos/viscoelastic/displacement-inverse-viscosity-weerdesteijn-2d_5ka_squashed-optimised-viscosity-iteration11-dx5km-nz160-dt50years-low-viscosityFalse.dat")
'''

disp_3d_new_gadi = np.loadtxt("/data/viscoelastic/3d_aspect_box/28.04.23_check_3d_newbranch_newgadiFD/displacement-weerdesteijn-3d.dat")

disp_3d_new_gadi_inherit = np.loadtxt("/data/viscoelastic/3d_aspect_box/05.03.24_check3d_newbranch_newgadiFD_inheritance/displacement-weerdesteijn-3d.dat")


# resolution/dt testing 08.03.24 new branch new FD on gadi
folder_resdt = "/data/viscoelastic/3d_aspect_box/14.03.24_displacement_griddt/"

# Refined surface mesh, varying resolution under ice
disp_3d_dx5_nz80_dt50 = np.loadtxt(folder_resdt+"displacement-weerdesteijn-3d-refinedsurfaceTrue-dx5km-nz80-dt50years.dat")
disp_3d_dx10_nz80_dt50 = np.loadtxt(folder_resdt+"displacement-weerdesteijn-3d-refinedsurfaceTrue-dx10km-nz80-dt50years.dat")
disp_3d_dx20_nz80_dt50 = np.loadtxt(folder_resdt+"displacement-weerdesteijn-3d-refinedsurfaceTrue-dx20km-nz80-dt50years.dat")

# Structured surface mesh
disp_3d_struc_dx50_nz80_dt50 = np.loadtxt(folder_resdt+"displacement-weerdesteijn-3d-refinedsurfaceFalse-dx50km-nz80-dt50years.dat")
disp_3d_struc_dx25_nz80_dt50 = np.loadtxt(folder_resdt+"displacement-weerdesteijn-3d-refinedsurfaceFalse-dx25km-nz80-dt50years.dat")
disp_3d_struc_dx12_nz80_dt50 = np.loadtxt(folder_resdt+"displacement-weerdesteijn-3d-refinedsurfaceFalse-dx12km-nz80-dt50years.dat")
# Structured surface mesh with sharper ice transition (8 * 5km wavelength)
disp_3d_struc_dx50_nz80_dt50_sharpice = np.loadtxt(folder_resdt+"displacement-weerdesteijn-3d-refinedsurfaceFalse-dx50km-sharpice-nz80-dt50years.dat")

# Refined surface mesh (dx = 5 km), varying vertical resolution
disp_3d_dx5_nz20_dt50 = np.loadtxt(folder_resdt+"displacement-weerdesteijn-3d-refinedsurfaceTrue-dx5km-nz20-dt50years.dat")
disp_3d_dx5_nz40_dt50 = np.loadtxt(folder_resdt+"displacement-weerdesteijn-3d-refinedsurfaceTrue-dx5km-nz40-dt50years.dat")
disp_3d_dx5_nz160_dt50 = np.loadtxt(folder_resdt+"displacement-weerdesteijn-3d-refinedsurfaceTrue-dx5km-nz160-dt50years.dat")
disp_3d_dx5_nz160_dt50_50ka = np.loadtxt(folder_resdt+"displacement-weerdesteijn-3d-from50ka-refinedsurfaceTrue-dx5km-nz160-dt50years.dat")

# Refined surface mesh (dt = 5 km), varying dt
disp_3d_dx5_nz80_dt100 = np.loadtxt(folder_resdt+"displacement-weerdesteijn-3d-refinedsurfaceTrue-dx5km-nz80-dt100.0years.dat")
disp_3d_dx5_nz80_dt200 = np.loadtxt(folder_resdt+"displacement-weerdesteijn-3d-refinedsurfaceTrue-dx5km-nz80-dt200.0years.dat")
disp_3d_dx5_nz80_dt400 = np.loadtxt(folder_resdt+"displacement-weerdesteijn-3d-refinedsurfaceTrue-dx5km-nz80-dt400.0years.dat")
disp_3d_dx5_nz80_dt800 = np.loadtxt(folder_resdt+"displacement-weerdesteijn-3d-refinedsurfaceTrue-dx5km-nz80-dt800.0years.dat")

# Refined box mesh, varying resolution under ice
disp_3d_dxz2pt5_dt50 = np.loadtxt(folder_resdt+"displacement-weerdesteijn-3d-refinedbox-isodxz2km-dt50years.dat")
disp_3d_dxz5_dt50 = np.loadtxt(folder_resdt+"displacement-weerdesteijn-3d-refinedbox-isodxz5km-dt50years.dat")
disp_3d_dxz6pt25_dt50 = np.loadtxt(folder_resdt+"displacement-weerdesteijn-3d-refinedbox-isodxz6km-dt50years.dat")
disp_3d_dxz10_dt50 = np.loadtxt(folder_resdt+"displacement-weerdesteijn-3d-refinedbox-isodxz10km-dt50years.dat")
disp_3d_dxz20_dt50 = np.loadtxt(folder_resdt+"displacement-weerdesteijn-3d-refinedbox-isodxz20km-dt50years.dat")



# 3d tanh 24.09.24
folder_3dtanh='/data/viscoelastic/3d_aspect_box/24.09.24_displacement_3d_verticaltanh/'
disp_3d_nz40_tanh5000 = np.loadtxt(folder_3dtanh+"displacement-weerdesteijn-3d-fixtanhdepth-refinedsurfaceTrue-dx5km-nz40-dt50years-tanh5000.0.dat")
disp_3d_nz80_tanh5000 = np.loadtxt(folder_3dtanh+"displacement-weerdesteijn-3d-fixtanhdepth-refinedsurfaceTrue-dx5km-nz80-dt50years-tanh5000.0.dat")
disp_3d_nz160_tanh5000 = np.loadtxt(folder_3dtanh+"displacement-weerdesteijn-3d-fixtanhdepth-refinedsurfaceTrue-dx5km-nz160-dt50years-tanh5000.0.dat")
disp_3d_nz40_tanh10000 = np.loadtxt(folder_3dtanh+"displacement-weerdesteijn-3d-fixtanhdepth-refinedsurfaceTrue-dx5km-nz40-dt50years-tanh10000.0.dat")
disp_3d_nz80_tanh10000 = np.loadtxt(folder_3dtanh+"displacement-weerdesteijn-3d-fixtanhdepth-refinedsurfaceTrue-dx5km-nz80-dt50years-tanh10000.0.dat")
disp_3d_nz160_tanh10000 = np.loadtxt(folder_3dtanh+"displacement-weerdesteijn-3d-fixtanhdepth-refinedsurfaceTrue-dx5km-nz160-dt50years-tanh10000.0.dat")

disp_3d_nz80default_notanh_log10visc = np.loadtxt(folder_3dtanh+"displacement-weerdesteijn-3d-defaultlogvisc-refinedsurfaceTrue-dx5km-nz80-dt50years-tanhNone.dat")
disp_3d_nz80default_notanh_normalvisc = np.loadtxt(folder_3dtanh+"displacement-weerdesteijn-3d-default_normalvisc-refinedsurfaceTrue-dx5km-nz80-dt50years-tanhNone.dat")
print("check tolerances")
#print(disp_drhog_iso_nolith_func[1][disp_drhog_iso_nolith_func[2],1:])
#print(len(disp_drhog_iso_nolith_func[1][disp_drhog_iso_nolith_func[2],1:]))
#print(np.allclose(disp_oldFD_long_gradmesh_TDG2_rhog_isostatic_nolith_func[1][disp_oldFD_long_gradmesh_TDG2_rhog_isostatic_nolith_func[2], 1:1000], disp_drhog_iso_nolith_func[1][disp_drhog_iso_nolith_func[2], 1:1000]))
#assert np.allclose(disp_oldFD_long_gradmesh_TDG2_rhog_isostatic_nolith_func[1][:1000], disp_drhog_iso_nolith_func[1][:1000])

#disp_drhog_iso_nolith_100ka = plot_time("/data/free_surface/aspect_box/15.01.24_832cores_viscoelastic_weerdesteijn_aspectbox_dx5km_nz80scaled_a4_dt50years_dtout25000years_Tend330000years_extruded_zhongprefactor_oldFD_TDG2interp_strong1e10_drhorho1_isostatic_nolith_from100ka/displacement_oldvom_arrays.csv", start=100e3)

# disp 3d 28.11.24 check
folder_3d_check_nov24 = "/data/viscoelastic/3d_aspect_box/28.11.24_displacement_3d_check/"
disp_3d_nz640_check = np.loadtxt(folder_3d_check_nov24+"displacement-weerdesteijn-3d-default_normalvisc-refinedsurfaceTrue-dx5km-nz640-dt50years-tanhNone.dat")
disp_3d_nz320_check = np.loadtxt(folder_3d_check_nov24+"displacement-weerdesteijn-3d-default_normalvisc-refinedsurfaceTrue-dx5km-nz320-dt50years-tanhNone.dat")
disp_3d_nz160_check = np.loadtxt(folder_3d_check_nov24+"displacement-weerdesteijn-3d-default_normalvisc-refinedsurfaceTrue-dx5km-nz160-dt50years-tanhNone.dat")
disp_3d_nz80_check = np.loadtxt(folder_3d_check_nov24+"displacement-weerdesteijn-3d-default_normalvisc-refinedsurfaceTrue-dx5km-nz80-dt50years-tanhNone.dat")
disp_3d_nz40_check = np.loadtxt(folder_3d_check_nov24+"displacement-weerdesteijn-3d-default_normalvisc-refinedsurfaceTrue-dx5km-nz40-dt50years-tanhNone.dat")
disp_3d_nz20_check = np.loadtxt(folder_3d_check_nov24+"displacement-weerdesteijn-3d-default_normalvisc-refinedsurfaceTrue-dx5km-nz20-dt50years-tanhNone.dat")
# 28.11.24 as above check with squashed vertical mesh...!
disp_3d_nz80_check_squash = np.loadtxt(folder_3d_check_nov24+"displacement-weerdesteijn-3d-default_normalvisc_vertsqu-refinedsurfaceTrue-dx5km-nz80-dt50years-tanhNone.dat")

# 11.12.24 P0dg layers check
folder_3d_check_DG0_dec24 = "/data/viscoelastic/3d_aspect_box/11.12.24_check_P0DGlayers/"
disp_3d_DG0_nz5 = np.loadtxt(folder_3d_check_DG0_dec24+"displacement-weerdesteijn-3d-P0DGprofiles_gamg-refinedsurfaceTrue-dx5km-nz5perlayer-dt50years-tanhNone-vertsquFalse.dat")
disp_3d_DG0_nz8 = np.loadtxt(folder_3d_check_DG0_dec24+"displacement-weerdesteijn-3d-P0DGprofiles_gamg-refinedsurfaceTrue-dx5km-nz8perlayer-dt50years-tanhNone-vertsquFalse.dat")
disp_3d_DG0_nz10 = np.loadtxt(folder_3d_check_DG0_dec24+"displacement-weerdesteijn-3d-P0DGprofiles_gamg-refinedsurfaceTrue-dx5km-nz10perlayer-dt50years-tanhNone-vertsquFalse.dat")
disp_3d_DG0_nz20 = np.loadtxt(folder_3d_check_DG0_dec24+"displacement-weerdesteijn-3d-P0DGprofiles_gamg-refinedsurfaceTrue-dx5km-nz20perlayer-dt50years-tanhNone-vertsquFalse.dat")
disp_3d_DG0_nz40 = np.loadtxt(folder_3d_check_DG0_dec24+"displacement-weerdesteijn-3d-P0DGprofiles_gamg-refinedsurfaceTrue-dx5km-nz40perlayer-dt50years-tanhNone-vertsquFalse.dat")

# 12.12.24 P0dg layers check
folder_3d_check_P1layer_dec24 = "/data/viscoelastic/3d_aspect_box/12.12.24_check_P1layers/"
disp_3d_P1_nz5 = np.loadtxt(folder_3d_check_P1layer_dec24+"displacement-weerdesteijn-3d-P1profiles_gamg-refinedsurfaceTrue-dx5km-nz5perlayer-dt50years-tanhNone-vertsquFalse.dat")
disp_3d_P1_nz8 = np.loadtxt(folder_3d_check_P1layer_dec24+"displacement-weerdesteijn-3d-P1profiles_gamg-refinedsurfaceTrue-dx5km-nz8perlayer-dt50years-tanhNone-vertsquFalse.dat")
disp_3d_P1_nz10 = np.loadtxt(folder_3d_check_P1layer_dec24+"displacement-weerdesteijn-3d-P1profiles_gamg-refinedsurfaceTrue-dx5km-nz10perlayer-dt50years-tanhNone-vertsquFalse.dat")
disp_3d_P1_nz20 = np.loadtxt(folder_3d_check_P1layer_dec24+"displacement-weerdesteijn-3d-P1profiles_gamg-refinedsurfaceTrue-dx5km-nz20perlayer-dt50years-tanhNone-vertsquFalse.dat")
disp_3d_P1_nz40 = np.loadtxt(folder_3d_check_P1layer_dec24+"displacement-weerdesteijn-3d-P1profiles_gamg-refinedsurfaceTrue-dx5km-nz40perlayer-dt50years-tanhNone-vertsquFalse.dat")

# 13.12.24 P0dg layers icetanh
folder_3d_DG0_dec24_icetanh = "/data/viscoelastic/3d_aspect_box/13.12.24_check_P0dglayers_icetanh/"
disp_3d_DGO_nz5_icetanh1km_dt800 = np.loadtxt(folder_3d_DG0_dec24_icetanh+"displacement-weerdesteijn-3d-P0DGprofiles_gamg_icetanh1km-refinedsurfaceTrue-dx5km-nz5perlayer-dt800.0years-tanhNone-vertsquFalse.dat")
disp_3d_DGO_nz5_icetanh2km_dt800 = np.loadtxt(folder_3d_DG0_dec24_icetanh+"displacement-weerdesteijn-3d-P0DGprofiles_gamg_icetanh2km-refinedsurfaceTrue-dx5km-nz5perlayer-dt800.0years-tanhNone-vertsquFalse.dat")
disp_3d_DGO_nz5_icetanh15km_dt800 = np.loadtxt(folder_3d_DG0_dec24_icetanh+"displacement-weerdesteijn-3d-P0DGprofiles_gamg_icetanh15km-refinedsurfaceTrue-dx5km-nz5perlayer-dt800.0years-tanhNone-vertsquFalse.dat")
disp_3d_DGO_nz5_icetanh15km_dt400 = np.loadtxt(folder_3d_DG0_dec24_icetanh+"displacement-weerdesteijn-3d-P0DGprofiles_gamg_icetanh15km-refinedsurfaceTrue-dx5km-nz5perlayer-dt400.0years-tanhNone-vertsquFalse.dat")

# P1 centred profile g = 9.815
folder_3d_check_P1layer_dec24_g = "/data/viscoelastic/3d_aspect_box/13.12.24_check_P1layers_g_rho1/"
disp_3d_P1_nz20_g = np.loadtxt(folder_3d_check_P1layer_dec24_g+"displacement-weerdesteijn-3d-P1profiles_gamg_g9pt815-refinedsurfaceTrue-dx5km-nz20perlayer-dt50years-tanhNone-vertsquFalse.dat")
disp_3d_P1_nz20_g_nofsrho1 = np.loadtxt(folder_3d_check_P1layer_dec24_g+"displacement-weerdesteijn-3d-P1profiles_gamg_g9pt815_nofsrho1-refinedsurfaceTrue-dx5km-nz20perlayer-dt50years-tanhNone-vertsquFalse.dat")
disp_3d_P1_nz20_g_nofsrho1_norho1 = np.loadtxt(folder_3d_check_P1layer_dec24_g+"displacement-weerdesteijn-3d-P1profiles_gamg_g9pt815_nofsrho1_norho1-refinedsurfaceTrue-dx5km-nz20perlayer-dt50years-tanhNone-vertsquFalse.dat")

# DG0 rho1 advected
folder_3d_DG0_rho1adv_dec24 = "/data/viscoelastic/3d_aspect_box/18.12.24_displacement_DG0_rho1adv/"
disp_3d_DG0_nz5_rho1adv = np.loadtxt(folder_3d_DG0_rho1adv_dec24+"displacement-weerdesteijn-3d-P0DGprofiles_gamg_icetanh15km_rho1_adv-refinedsurfaceTrue-dx5km-nz5perlayer-dt800.0years-tanhNone-vertsquFalse.dat")
disp_3d_DG0_nz10_rho1adv = np.loadtxt(folder_3d_DG0_rho1adv_dec24+"displacement-weerdesteijn-3d-P0DGprofiles_gamg_icetanh15km_rho1_adv-refinedsurfaceTrue-dx5km-nz10perlayer-dt800.0years-tanhNone-vertsquFalse.dat")
disp_3d_DG0_nz20_rho1adv = np.loadtxt(folder_3d_DG0_rho1adv_dec24+"displacement-weerdesteijn-3d-P0DGprofiles_gamg_icetanh15km_rho1_adv-refinedsurfaceTrue-dx5km-nz20perlayer-dt800.0years-tanhNone-vertsquFalse.dat")

disp_3d_DG0_nz5_rho1adv_bc0 = np.loadtxt(folder_3d_DG0_rho1adv_dec24+"displacement-weerdesteijn-3d-P0DGprofiles_gamg_icetanh15km_rho1_adv_rhobc0-refinedsurfaceTrue-dx5km-nz5perlayer-dt800.0years-tanhNone-vertsquFalse.dat")
disp_3d_DG0_nz5_rho1adv_bcdiff = np.loadtxt(folder_3d_DG0_rho1adv_dec24+"displacement-weerdesteijn-3d-P0DGprofiles_gamg_icetanh15km_rho1_adv_rhobcextdens-refinedsurfaceTrue-dx5km-nz5perlayer-dt800.0years-tanhNone-vertsquFalse.dat")
disp_3d_DG0_nz10_rho1adv_bcdiff = np.loadtxt(folder_3d_DG0_rho1adv_dec24+"displacement-weerdesteijn-3d-P0DGprofiles_gamg_icetanh15km_rho1_adv_rhobcextdens-refinedsurfaceTrue-dx5km-nz10perlayer-dt800.0years-tanhNone-vertsquFalse.dat")
disp_3d_DG0_nz20_rho1adv_bcdiff = np.loadtxt(folder_3d_DG0_rho1adv_dec24+"displacement-weerdesteijn-3d-P0DGprofiles_gamg_icetanh15km_rho1_adv_rhobcextdens-refinedsurfaceTrue-dx5km-nz20perlayer-dt800.0years-tanhNone-vertsquFalse.dat")

disp_3d_DG0_nz5_rho1adv_bcdiff_nofs = np.loadtxt(folder_3d_DG0_rho1adv_dec24+"displacement-weerdesteijn-3d-P0DGprofiles_gamg_icetanh15km_rho1_adv_rhobcextdens_nofs-refinedsurfaceTrue-dx5km-nz5perlayer-dt800.0years-tanhNone-vertsquFalse.dat")

# P1DG density advection
disp_3d_DG0_nz5_rho1adv_bcdiff_nofs_p1dg = np.loadtxt(folder_3d_DG0_rho1adv_dec24+"displacement-weerdesteijn-3d-P0DGprofiles_gamg_icetanh15km_rho1_adv_rhobcextdens_nofs_P1DG-refinedsurfaceTrue-dx5km-nz5perlayer-dt800.0years-tanhNone-vertsquFalse.dat")
disp_3d_DG0_nz10_rho1adv_bcdiff_nofs_p1dg = np.loadtxt(folder_3d_DG0_rho1adv_dec24+"displacement-weerdesteijn-3d-P0DGprofiles_gamg_icetanh15km_rho1_adv_rhobcextdens_nofs_P1DG-refinedsurfaceTrue-dx5km-nz10perlayer-dt800.0years-tanhNone-vertsquFalse.dat")
disp_3d_DG0_nz20_rho1adv_bcdiff_nofs_p1dg = np.loadtxt(folder_3d_DG0_rho1adv_dec24+"displacement-weerdesteijn-3d-P0DGprofiles_gamg_icetanh15km_rho1_adv_rhobcextdens_nofs_P1DG-refinedsurfaceTrue-dx5km-nz20perlayer-dt800.0years-tanhNone-vertsquFalse.dat")

# ibp interior facet hyrostatic prestress and rho1b (diff rho surface) ice tanh 1km Jan 2025
folder_3d_DG0_ibp_jan24 = "/data/viscoelastic/3d_aspect_box/23.01.25_disp_intfacet_hydpre_rho1_tanh1km/"
disp_3d_DG0_ibp_nz5_icetanh1 = np.loadtxt(folder_3d_DG0_ibp_jan24+"displacement-weerdesteijn-3d-P0DGprofiles_gamg_icetanh1km_fs_intfacetminus_rho1ibp_rho1diffdst_impdisp-refinedsurfaceTrue-dx5km-nz5perlayer-dt800.0years-tanhNone-vertsquFalse.dat")
disp_3d_DG0_ibp_nz8_icetanh1 = np.loadtxt(folder_3d_DG0_ibp_jan24+"displacement-weerdesteijn-3d-P0DGprofiles_gamg_icetanh1km_fs_intfacetminus_rho1ibp_rho1diffdst_impdisp-refinedsurfaceTrue-dx5km-nz8perlayer-dt800.0years-tanhNone-vertsquFalse.dat")
disp_3d_DG0_ibp_nz40_icetanh1 = np.loadtxt(folder_3d_DG0_ibp_jan24+"displacement-weerdesteijn-3d-P0DGprofiles_gamg_icetanh1km_fs_intfacetminus_rho1ibp_rho1diffdst_impdisp-refinedsurfaceTrue-dx5km-nz40perlayer-dt800.0years-tanhNone-vertsquFalse.dat")

# ibp interior facet hyrostatic prestress and rho1b (diff rho surface) ice tanh 2km Jan 2025
folder_3d_DG0_ibp_jan24_icetanh2 = "/data/viscoelastic/3d_aspect_box/23.01.25_disp_intfacet_hydpre_rho1_tanh2km/"
disp_3d_DG0_ibp_nz5_icetanh2 = np.loadtxt(folder_3d_DG0_ibp_jan24_icetanh2+"displacement-weerdesteijn-3d-P0DGprofiles_gamg_icetanh2km_fs_intfacetminus_rho1ibp_rho1diffdst_impdisp-refinedsurfaceTrue-dx5km-nz5perlayer-dt800.0years-tanhNone-vertsquFalse.dat")
disp_3d_DG0_ibp_nz8_icetanh2 = np.loadtxt(folder_3d_DG0_ibp_jan24_icetanh2+"displacement-weerdesteijn-3d-P0DGprofiles_gamg_icetanh2km_fs_intfacetminus_rho1ibp_rho1diffdst_impdisp-refinedsurfaceTrue-dx5km-nz8perlayer-dt800.0years-tanhNone-vertsquFalse.dat")
disp_3d_DG0_ibp_nz20_icetanh2 = np.loadtxt(folder_3d_DG0_ibp_jan24_icetanh2+"displacement-weerdesteijn-3d-P0DGprofiles_gamg_icetanh2km_fs_intfacetminus_rho1ibp_rho1diffdst_impdisp-refinedsurfaceTrue-dx5km-nz20perlayer-dt800.0years-tanhNone-vertsquFalse.dat")
disp_3d_DG0_ibp_nz40_icetanh2 = np.loadtxt(folder_3d_DG0_ibp_jan24_icetanh2+"displacement-weerdesteijn-3d-P0DGprofiles_gamg_icetanh2km_fs_intfacetminus_rho1ibp_rho1diffdst_impdisp-refinedsurfaceTrue-dx5km-nz40perlayer-dt800.0years-tanhNone-vertsquFalse.dat")

# ibp interior facet hydrostatic prestress and rho1g (explicit disp) (diff rho surface) icetanh 1km dt check  25Jan2025
folder_3d_DG0_ibp_jan24_icetanh1_dt = "/data/viscoelastic/3d_aspect_box/25.01.25_disp_intfacet_hyrdpre_rho1_tanh1km_dt/"
disp_3d_DG0_ibp_nz40_icetanh1_dt200 = np.loadtxt(folder_3d_DG0_ibp_jan24_icetanh1_dt+"displacement-weerdesteijn-3d-P0DGprofiles_gamg_icetanh1km_fs_intfacetminus_rho1ibp_rho1diffdst_expdisp-refinedsurfaceTrue-dx5km-nz40perlayer-dt200.0years-tanhNone-vertsquFalse.dat")
disp_3d_DG0_ibp_nz40_icetanh1_dt400 = np.loadtxt(folder_3d_DG0_ibp_jan24_icetanh1_dt+"displacement-weerdesteijn-3d-P0DGprofiles_gamg_icetanh1km_fs_intfacetminus_rho1ibp_rho1diffdst_expdisp-refinedsurfaceTrue-dx5km-nz40perlayer-dt400.0years-tanhNone-vertsquFalse.dat")
disp_3d_DG0_ibp_nz40_icetanh1_dt1000 = np.loadtxt(folder_3d_DG0_ibp_jan24_icetanh1_dt+"displacement-weerdesteijn-3d-P0DGprofiles_gamg_icetanh1km_fs_intfacetminus_rho1ibp_rho1diffdst_expdisp-refinedsurfaceTrue-dx5km-nz40perlayer-dt1000.0years-tanhNone-vertsquFalse.dat")
disp_3d_DG0_ibp_nz40_icetanh1_dt5000 = np.loadtxt(folder_3d_DG0_ibp_jan24_icetanh1_dt+"displacement-weerdesteijn-3d-P0DGprofiles_gamg_icetanh1km_fs_intfacetminus_rho1ibp_rho1diffdst_expdisp-refinedsurfaceTrue-dx5km-nz40perlayer-dt5000.0years-tanhNone-vertsquFalse.dat")
disp_3d_DG0_ibp_nz40_icetanh1_dt10000 = np.loadtxt(folder_3d_DG0_ibp_jan24_icetanh1_dt+"displacement-weerdesteijn-3d-P0DGprofiles_gamg_icetanh1km_fs_intfacetminus_rho1ibp_rho1diffdst_expdisp-refinedsurfaceTrue-dx5km-nz40perlayer-dt10000.0years-tanhNone-vertsquFalse.dat")

# ibp interior facet hydrostatic prestress and rho1g (diff rho surface) icetanh 1km dt, implicit displacement for rho1 (fails symmetric check for some combinations, nz 10/layer, dt > 5000a)  25Jan2025
folder_3d_DG0_ibp_jan24_icetanh1_dt_impdisp = "/data/viscoelastic/3d_aspect_box/25.01.25_disp_intfacet_hyrdpre_rho1_tanh1km_dt_impdisp/"
disp_3d_DG0_ibp_nz40_icetanh1_dt200_impdisp = np.loadtxt(folder_3d_DG0_ibp_jan24_icetanh1_dt_impdisp+"displacement-weerdesteijn-3d-P0DGprofiles_gamg_icetanh1km_fs_intfacetminus_rho1ibp_rho1diffdst_impdisp-refinedsurfaceTrue-dx5km-nz40perlayer-dt200.0years-tanhNone-vertsquFalse.dat")
disp_3d_DG0_ibp_nz40_icetanh1_dt400_impdisp = np.loadtxt(folder_3d_DG0_ibp_jan24_icetanh1_dt_impdisp+"displacement-weerdesteijn-3d-P0DGprofiles_gamg_icetanh1km_fs_intfacetminus_rho1ibp_rho1diffdst_impdisp-refinedsurfaceTrue-dx5km-nz40perlayer-dt400.0years-tanhNone-vertsquFalse.dat")
disp_3d_DG0_ibp_nz40_icetanh1_dt800_impdisp = np.loadtxt(folder_3d_DG0_ibp_jan24_icetanh1_dt_impdisp+"displacement-weerdesteijn-3d-P0DGprofiles_gamg_icetanh1km_fs_intfacetminus_rho1ibp_rho1diffdst_impdisp-refinedsurfaceTrue-dx5km-nz40perlayer-dt800.0years-tanhNone-vertsquFalse.dat")
disp_3d_DG0_ibp_nz40_icetanh1_dt1000_impdisp = np.loadtxt(folder_3d_DG0_ibp_jan24_icetanh1_dt_impdisp+"displacement-weerdesteijn-3d-P0DGprofiles_gamg_icetanh1km_fs_intfacetminus_rho1ibp_rho1diffdst_impdisp-refinedsurfaceTrue-dx5km-nz40perlayer-dt1000.0years-tanhNone-vertsquFalse.dat")


# DG0 ibp, no free surface term, rho1 ibp no ds top, 31.01.25
folder_3d_DG0_ibp_jan25_nofs_norho1dst = "/data/viscoelastic/3d_aspect_box/31.01.25_disp_DG0_nofs_rho1ibpnodst/"
disp_3d_DG0_ibp_nz5_nofs_norho1dst = np.loadtxt(folder_3d_DG0_ibp_jan25_nofs_norho1dst+"displacement-weerdesteijn-3d-P0DGprofiles_gamg_icetanh1km_fs_intfacetminus_rho1ibp_expdisp_mualphajump_symthresh1e-2_gmresgamg_nofsnorho1diffdst-refinedsurfaceTrue-dx5km-nz5perlayer-dt1000.0years-tanhNone-vertsquFalse.dat")
disp_3d_DG0_ibp_nz10_nofs_norho1dst = np.loadtxt(folder_3d_DG0_ibp_jan25_nofs_norho1dst+"displacement-weerdesteijn-3d-P0DGprofiles_gamg_icetanh1km_fs_intfacetminus_rho1ibp_expdisp_mualphajump_symthresh1e-2_gmresgamg_nofsnorho1diffdst-refinedsurfaceTrue-dx5km-nz10perlayer-dt1000.0years-tanhNone-vertsquFalse.dat")
disp_3d_DG0_ibp_nz20_nofs_norho1dst = np.loadtxt(folder_3d_DG0_ibp_jan25_nofs_norho1dst+"displacement-weerdesteijn-3d-P0DGprofiles_gamg_icetanh1km_fs_intfacetminus_rho1ibp_expdisp_mualphajump_symthresh1e-2_gmresgamg_nofsnorho1diffdst-refinedsurfaceTrue-dx5km-nz20perlayer-dt1000.0years-tanhNone-vertsquFalse.dat")
disp_3d_DG0_ibp_nz40_nofs_norho1dst = np.loadtxt(folder_3d_DG0_ibp_jan25_nofs_norho1dst+"displacement-weerdesteijn-3d-P0DGprofiles_gamg_icetanh1km_fs_intfacetminus_rho1ibp_expdisp_mualphajump_symthresh1e-2_gmresgamg_nofsnorho1diffdst-refinedsurfaceTrue-dx5km-nz40perlayer-dt1000.0years-tanhNone-vertsquFalse.dat")

# DG0, fs rho0, no rho1 (not ibp), 31.01.25
folder_3d_DG0_ibp_jan25_fsrho0_norho1 = "/data/viscoelastic/3d_aspect_box/31.01.25_disp_DG0_fsrho0_norho1/"
disp_3d_DG0_ibp_nz5_fsrho0_norho1 = np.loadtxt(folder_3d_DG0_ibp_jan25_fsrho0_norho1+"displacement-weerdesteijn-3d-P0DGprofiles_gamg_icetanh1km_fs_intfacetminus_gmresgamg_fsrho0_norho1-refinedsurfaceTrue-dx5km-nz5perlayer-dt1000.0years-tanhNone-vertsquFalse.dat") 
disp_3d_DG0_ibp_nz10_fsrho0_norho1 = np.loadtxt(folder_3d_DG0_ibp_jan25_fsrho0_norho1+"displacement-weerdesteijn-3d-P0DGprofiles_gamg_icetanh1km_fs_intfacetminus_gmresgamg_fsrho0_norho1-refinedsurfaceTrue-dx5km-nz10perlayer-dt1000.0years-tanhNone-vertsquFalse.dat") 
disp_3d_DG0_ibp_nz20_fsrho0_norho1 = np.loadtxt(folder_3d_DG0_ibp_jan25_fsrho0_norho1+"displacement-weerdesteijn-3d-P0DGprofiles_gamg_icetanh1km_fs_intfacetminus_gmresgamg_fsrho0_norho1-refinedsurfaceTrue-dx5km-nz20perlayer-dt1000.0years-tanhNone-vertsquFalse.dat") 
disp_3d_DG0_ibp_nz40_fsrho0_norho1 = np.loadtxt(folder_3d_DG0_ibp_jan25_fsrho0_norho1+"displacement-weerdesteijn-3d-P0DGprofiles_gamg_icetanh1km_fs_intfacetminus_gmresgamg_fsrho0_norho1-refinedsurfaceTrue-dx5km-nz40perlayer-dt1000.0years-tanhNone-vertsquFalse.dat") 

# DG0, no ibp: prestress adv, no rho1 (not ibp) 31.01.25
folder_3d_DG0_noibp_jan25_justprestressadv_norho1 = "/data/viscoelastic/3d_aspect_box/31.01.25_disp_DG0_prestressadvnoibp_norho1/"
disp_3d_DG0_noibp_nz5_jan25_justprestressadv_norho1 = np.loadtxt(folder_3d_DG0_noibp_jan25_justprestressadv_norho1+"displacement-weerdesteijn-3d-P0DGprofiles_gamg_icetanh1km_fs_intfacetminus_gmresgamg_prestressadv_noibp_norho1-refinedsurfaceTrue-dx5km-nz5perlayer-dt1000.0years-tanhNone-vertsquFalse.dat")

# P1, no ibp: prestress adv, rho1 05.02.25
folder_3d_P1_noibp_feb25_prestressadv_rho1 = "/data/viscoelastic/3d_aspect_box/05.02.25_disp_P1_prestressadvnoibp_rho1/"
disp_3d_P1_noibp_nz5_feb25_prestressadv_rho1 = np.loadtxt(folder_3d_P1_noibp_feb25_prestressadv_rho1+"displacement-weerdesteijn-3d-P1profiles_rho1adv_prestressadv_noibp_nofs-refinedsurfaceTrue-dx5km-nz5perlayer-dt1000.0years-tanhNone-vertsquFalse.dat")
disp_3d_P1_noibp_nz10_feb25_prestressadv_rho1 = np.loadtxt(folder_3d_P1_noibp_feb25_prestressadv_rho1+"displacement-weerdesteijn-3d-P1profiles_rho1adv_prestressadv_noibp_nofs-refinedsurfaceTrue-dx5km-nz10perlayer-dt1000.0years-tanhNone-vertsquFalse.dat")
disp_3d_P1_noibp_nz20_feb25_prestressadv_rho1 = np.loadtxt(folder_3d_P1_noibp_feb25_prestressadv_rho1+"displacement-weerdesteijn-3d-P1profiles_rho1adv_prestressadv_noibp_nofs-refinedsurfaceTrue-dx5km-nz20perlayer-dt1000.0years-tanhNone-vertsquFalse.dat")
disp_3d_P1_noibp_nz40_feb25_prestressadv_rho1 = np.loadtxt(folder_3d_P1_noibp_feb25_prestressadv_rho1+"displacement-weerdesteijn-3d-P1profiles_rho1adv_prestressadv_noibp_nofs-refinedsurfaceTrue-dx5km-nz40perlayer-dt1000.0years-tanhNone-vertsquFalse.dat")
# as above but dt change
disp_3d_P1_noibp_nz40_feb25_prestressadv_rho1_dt500 = np.loadtxt(folder_3d_P1_noibp_feb25_prestressadv_rho1+"displacement-weerdesteijn-3d-P1profiles_rho1adv_prestressadv_noibp_nofs-refinedsurfaceTrue-dx5km-nz40perlayer-dt500.0years-tanhNone-vertsquFalse.dat")

# P1, ibp: prestress adv fs rho0, rho1 05.02.25
folder_3d_P1_ibp_feb25_fsrho0_rho1 = "/data/viscoelastic/3d_aspect_box/05.02.25_disp_P1_fsrho0_rho1/"
disp_3d_P1_ibp_nz5_feb25_fsrho0_rho1 = np.loadtxt(folder_3d_P1_ibp_feb25_fsrho0_rho1+"displacement-weerdesteijn-3d-P1profiles_rho1adv_prestressadv_ibp_justfsrho0-refinedsurfaceTrue-dx5km-nz5perlayer-dt1000.0years-tanhNone-vertsquFalse.dat")
disp_3d_P1_ibp_nz10_feb25_fsrho0_rho1 = np.loadtxt(folder_3d_P1_ibp_feb25_fsrho0_rho1+"displacement-weerdesteijn-3d-P1profiles_rho1adv_prestressadv_ibp_justfsrho0-refinedsurfaceTrue-dx5km-nz10perlayer-dt1000.0years-tanhNone-vertsquFalse.dat")
disp_3d_P1_ibp_nz20_feb25_fsrho0_rho1 = np.loadtxt(folder_3d_P1_ibp_feb25_fsrho0_rho1+"displacement-weerdesteijn-3d-P1profiles_rho1adv_prestressadv_ibp_justfsrho0-refinedsurfaceTrue-dx5km-nz20perlayer-dt1000.0years-tanhNone-vertsquFalse.dat")
disp_3d_P1_ibp_nz40_feb25_fsrho0_rho1 = np.loadtxt(folder_3d_P1_ibp_feb25_fsrho0_rho1+"displacement-weerdesteijn-3d-P1profiles_rho1adv_prestressadv_ibp_justfsrho0-refinedsurfaceTrue-dx5km-nz40perlayer-dt1000.0years-tanhNone-vertsquFalse.dat")
disp_3d_P1_ibp_nz80_feb25_fsrho0_rho1 = np.loadtxt(folder_3d_P1_ibp_feb25_fsrho0_rho1+"displacement-weerdesteijn-3d-P1profiles_rho1adv_prestressadv_ibp_justfsrho0-refinedsurfaceTrue-dx5km-nz80perlayer-dt1000.0years-tanhNone-vertsquFalse.dat")

# P1 old mesh, ibp fs, rho1 06.02.25
folder_3d_P1_ibp_feb25_fsrho0_rho1_oldmesh ="/data/viscoelastic/3d_aspect_box/06.02.25_oldmesh_P1_fsrho0_rho1_vertsquFalse/"
disp_3d_P1_ibp_nz20_feb25_fsrho0_rho1_oldmesh = np.loadtxt(folder_3d_P1_ibp_feb25_fsrho0_rho1_oldmesh+"displacement-weerdesteijn-3d-P1_oldmesh_fsrho0-refinedsurfaceTrue-dx5km-nz20-dt1000.0years-tanhNone-vertsquFalse.dat")
disp_3d_P1_ibp_nz40_feb25_fsrho0_rho1_oldmesh = np.loadtxt(folder_3d_P1_ibp_feb25_fsrho0_rho1_oldmesh+"displacement-weerdesteijn-3d-P1_oldmesh_fsrho0-refinedsurfaceTrue-dx5km-nz40-dt1000.0years-tanhNone-vertsquFalse.dat")
disp_3d_P1_ibp_nz80_feb25_fsrho0_rho1_oldmesh = np.loadtxt(folder_3d_P1_ibp_feb25_fsrho0_rho1_oldmesh+"displacement-weerdesteijn-3d-P1_oldmesh_fsrho0-refinedsurfaceTrue-dx5km-nz80-dt1000.0years-tanhNone-vertsquFalse.dat")
disp_3d_P1_ibp_nz160_feb25_fsrho0_rho1_oldmesh = np.loadtxt(folder_3d_P1_ibp_feb25_fsrho0_rho1_oldmesh+"displacement-weerdesteijn-3d-P1_oldmesh_fsrho0-refinedsurfaceTrue-dx5km-nz160-dt1000.0years-tanhNone-vertsquFalse.dat")
disp_3d_P1_ibp_nz320_feb25_fsrho0_rho1_oldmesh = np.loadtxt(folder_3d_P1_ibp_feb25_fsrho0_rho1_oldmesh+"displacement-weerdesteijn-3d-P1_oldmesh_fsrho0-refinedsurfaceTrue-dx5km-nz320-dt1000.0years-tanhNone-vertsquFalse.dat")

# Internal variable nz comparison - plotted on 6th March 2025 (but run on 22nd of feb 2025 ish)
folder_3d_internal_variable_nz = "/data/viscoelastic/3d_aspect_box/06.03.25_internalvariable_dt1ka_bulk1e13_nzcomparison/" 
disp_3d_intvar_dt1ka_k1e13_nz1_mar25 = np.loadtxt(folder_3d_internal_variable_nz+"displacement-weerdesteijn-3d-internalvariable-symmult-refinedsurfaceTrue-dx5.0km-nz1perlayer-dt1000.0years-bulk10000000000000.0.dat")
disp_3d_intvar_dt1ka_k1e13_nz2_mar25 = np.loadtxt(folder_3d_internal_variable_nz+"displacement-weerdesteijn-3d-internalvariable-symmult-refinedsurfaceTrue-dx5.0km-nz2perlayer-dt1000.0years-bulk10000000000000.0.dat")
disp_3d_intvar_dt1ka_k1e13_nz4_mar25 = np.loadtxt(folder_3d_internal_variable_nz+"displacement-weerdesteijn-3d-internalvariable-symmult-refinedsurfaceTrue-dx5.0km-nz4perlayer-dt1000.0years-bulk10000000000000.0.dat")
disp_3d_intvar_dt1ka_k1e13_nz5_mar25 = np.loadtxt(folder_3d_internal_variable_nz+"displacement-weerdesteijn-3d-internalvariable-symmult-refinedsurfaceTrue-dx5.0km-nz5perlayer-dt1000.0years-bulk10000000000000.0.dat")
disp_3d_intvar_dt1ka_k1e13_nz8_mar25 = np.loadtxt(folder_3d_internal_variable_nz+"displacement-weerdesteijn-3d-internalvariable-symmult-refinedsurfaceTrue-dx5.0km-nz8perlayer-dt1000.0years-bulk10000000000000.0.dat")
disp_3d_intvar_dt1ka_k1e13_nz10_mar25 = np.loadtxt(folder_3d_internal_variable_nz+"displacement-weerdesteijn-3d-internalvariable-symmult-refinedsurfaceTrue-dx5.0km-nz10perlayer-dt1000.0years-bulk10000000000000.0.dat")
disp_3d_intvar_dt1ka_k1e13_nz20_mar25 = np.loadtxt(folder_3d_internal_variable_nz+"displacement-weerdesteijn-3d-internalvariable-symmult-refinedsurfaceTrue-dx5.0km-nz20perlayer-dt1000.0years-bulk10000000000000.0.dat")


# Internal variable bulk compressibility comparison - plotted on 6th March 2025 (but run on 22nd of feb 2025 ish)
folder_3d_internal_variable_bulk = "/data/viscoelastic/3d_aspect_box/06.03.25_internalvariable_dt1ka_nz5_bulkcomparison/"
disp_3d_intvar_dt1ka_nz5_k1e11_mar25 = np.loadtxt(folder_3d_internal_variable_bulk+"displacement-weerdesteijn-3d-internalvariable-symmult-refinedsurfaceTrue-dx5.0km-nz5perlayer-dt1000.0years-bulk100000000000.0.dat")
disp_3d_intvar_dt1ka_nz5_k1e12_mar25 = np.loadtxt(folder_3d_internal_variable_bulk+"displacement-weerdesteijn-3d-internalvariable-symmult-refinedsurfaceTrue-dx5.0km-nz5perlayer-dt1000.0years-bulk1000000000000.0.dat")
disp_3d_intvar_dt1ka_nz5_k1e13_mar25 = np.loadtxt(folder_3d_internal_variable_bulk+"displacement-weerdesteijn-3d-internalvariable-symmult-refinedsurfaceTrue-dx5.0km-nz5perlayer-dt1000.0years-bulk10000000000000.0.dat")
disp_3d_intvar_dt1ka_nz5_k1e14_mar25 = np.loadtxt(folder_3d_internal_variable_bulk+"displacement-weerdesteijn-3d-internalvariable-symmult-refinedsurfaceTrue-dx5.0km-nz5perlayer-dt1000.0years-bulk100000000000000.0.dat")


# Internal variablle dt comparison, ran on 6th march? but plotted on 14th march
folder_3d_internal_variable_dt = "/data/viscoelastic/3d_aspect_box/06.03.25_internalvariable_nz10_bulk1e13_dtcomp/"
disp_3d_intvar_nz10_k1e13_dt500a_mar25 = np.loadtxt(folder_3d_internal_variable_dt+"displacement-weerdesteijn-3d-internalvariable-symmult-refinedsurfaceTrue-dx5.0km-nz10perlayer-dt500.0years-bulk10000000000000.0.dat")
disp_3d_intvar_nz10_k1e13_dt1000a_mar25 = np.loadtxt(folder_3d_internal_variable_dt+"displacement-weerdesteijn-3d-internalvariable-symmult-refinedsurfaceTrue-dx5.0km-nz10perlayer-dt1000.0years-bulk10000000000000.0.dat")
disp_3d_intvar_nz10_k1e13_dt2000a_mar25 = np.loadtxt(folder_3d_internal_variable_dt+"displacement-weerdesteijn-3d-internalvariable-symmult-refinedsurfaceTrue-dx5.0km-nz10perlayer-dt2000.0years-bulk10000000000000.0.dat")
disp_3d_intvar_nz10_k1e13_dt5000a_mar25 = np.loadtxt(folder_3d_internal_variable_dt+"displacement-weerdesteijn-3d-internalvariable-symmult-refinedsurfaceTrue-dx5.0km-nz10perlayer-dt5000.0years-bulk10000000000000.0.dat")
disp_3d_intvar_nz10_k1e13_dt10000a_mar25 = np.loadtxt(folder_3d_internal_variable_dt+"displacement-weerdesteijn-3d-internalvariable-symmult-refinedsurfaceTrue-dx5.0km-nz10perlayer-dt10000.0years-bulk10000000000000.0.dat")


# Internal variable NONDIMENSIONAL dx comparison, ran on 7th march 2025? plotted on 14th march
folder_3d_internal_variable_nondim_dx = "/data/viscoelastic/3d_aspect_box/07.03.25_internalvariable_nondimensional_bulk1e13_dt1ka_dxcomp/"

disp_3d_intvar_nondim_k1e13_dt1ka_nz10_dx5_mar25 =np.loadtxt(folder_3d_internal_variable_nondim_dx+"displacement-weerdesteijn-3d-internalvariable-symmult_nondim-refinedsurfaceTrue-dx5.0km-nz10perlayer-dt1000.0years-bulk100.0-nondim.dat")
disp_3d_intvar_nondim_k1e13_dt1ka_nz10_dx10_mar25 =np.loadtxt(folder_3d_internal_variable_nondim_dx+"displacement-weerdesteijn-3d-internalvariable-symmult_nondim-refinedsurfaceTrue-dx10.0km-nz10perlayer-dt1000.0years-bulk100.0-nondim.dat")
disp_3d_intvar_nondim_k1e13_dt1ka_nz10_dx20_mar25 =np.loadtxt(folder_3d_internal_variable_nondim_dx+"displacement-weerdesteijn-3d-internalvariable-symmult_nondim-refinedsurfaceTrue-dx20.0km-nz10perlayer-dt1000.0years-bulk100.0-nondim.dat")
disp_3d_intvar_nondim_k1e13_dt1ka_nz10_dx40_mar25 =np.loadtxt(folder_3d_internal_variable_nondim_dx+"displacement-weerdesteijn-3d-internalvariable-symmult_nondim-refinedsurfaceTrue-dx40.0km-nz10perlayer-dt1000.0years-bulk100.0-nondim.dat")


# internal variable nondim check bulk 1000x ran on . plotted on 17th march 2025
folder_3d_internal_variable_nondim_bulk1000 = "/data/viscoelastic/3d_aspect_box/17.03.25_internalvariable_dt1ka-nz5_bulk1000_nondim/"
disp_3d_intvar_nondim_k1e14_dt1ka_nz10_dx5_mar25 =np.loadtxt(folder_3d_internal_variable_nondim_bulk1000+"displacement-weerdesteijn-3d-internalvariable-symmult_nondim-refinedsurfaceTrue-dx5.0km-nz10perlayer-dt1000.0years-bulk1000.0-nondim.dat")

displacement = displacement.to_numpy()
displacement_40 = displacement_40.to_numpy()
displacement_rhog = displacement_rhog.to_numpy()
displacement_zhong = displacement_zhong.to_numpy()
displacement_zhong_topid = displacement_zhong_topid.to_numpy()
displacement_zhong_topid_prestress = displacement_zhong_topid_prestress.to_numpy()
displacement_zhong_topid_prestress_pos = displacement_zhong_topid_prestress_pos.to_numpy()
displacement_zhong_topid_prestress_pos_nodrhog = displacement_zhong_topid_prestress_pos_nodrhog.to_numpy()
displacement_zhong_topid_prestress_pos_nodrhog_80 = displacement_zhong_topid_prestress_pos_nodrhog_80.to_numpy()
displacement_zhong_topid_prestress_pos_nodrhog_160 = displacement_zhong_topid_prestress_pos_nodrhog_160.to_numpy()
displacement_zhong_topid_nodrhog = displacement_zhong_topid_nodrhog.to_numpy()
displacement_zhong_topid_nodrhog_80 = displacement_zhong_topid_nodrhog_80.to_numpy()
disp_oldFD_surfadv_80 = disp_oldFD_surfadv_80.to_numpy()
disp_oldFD_surfadv_80_check = disp_oldFD_surfadv_80_check.to_numpy()
disp_oldFD_long = disp_oldFD_long.to_numpy()
disp_oldFD_long_rho1g = disp_oldFD_long_rho1g.to_numpy()
disp_oldFD_long_gradmesh = disp_oldFD_long_gradmesh.to_numpy()
disp_oldFD_long_gradmesh_TDG2 = disp_oldFD_long_gradmesh_TDG2.to_numpy()
disp_oldFD_long_gradmesh_TDG2_rho1g = disp_oldFD_long_gradmesh_TDG2_rho1g.to_numpy()
disp_oldFD_long_gradmesh_TDG2_strong = disp_oldFD_long_gradmesh_TDG2_strong.to_numpy()
disp_oldFD_long_gradmesh_TDG2_from64ka = disp_oldFD_long_gradmesh_TDG2_from64ka.to_numpy()
disp_oldFD_long_gradmesh_TDG2_strong_gradp = disp_oldFD_long_gradmesh_TDG2_strong_gradp.to_numpy()
disp_oldFD_long_gradmesh_TDG2_weak_scale = disp_oldFD_long_gradmesh_TDG2_weak_scale.to_numpy()
disp_oldFD_long_gradmesh_TDG2_from75_drhog = disp_oldFD_long_gradmesh_TDG2_from75_drhog.to_numpy()
disp_oldFD_long_gradmesh_TDG2_strong_scaleprevstress = disp_oldFD_long_gradmesh_TDG2_strong_scaleprevstress.to_numpy()
disp_oldFD_long_gradmesh_TDG2_drhog = disp_oldFD_long_gradmesh_TDG2_drhog.to_numpy()
disp_oldFD_long_gradmesh_TDG2_drhog_rho1g = disp_oldFD_long_gradmesh_TDG2_drhog_rho1g.to_numpy()
disp_oldFD_long_gradmesh_TDG2_drhog_rho1g_strong = disp_oldFD_long_gradmesh_TDG2_drhog_rho1g_strong.to_numpy()
disp_oldFD_long_gradmesh_TDG2_nodrhog = disp_oldFD_long_gradmesh_TDG2_nodrhog.to_numpy()
disp_oldFD_long_gradmesh_TDG2_zerodrhog_norho1 = disp_oldFD_long_gradmesh_TDG2_zerodrhog_norho1.to_numpy()
disp_oldFD_long_gradmesh_TDG2_zerodrhog_rho1 = disp_oldFD_long_gradmesh_TDG2_zerodrhog_rho1.to_numpy()
disp_oldFD_long_gradmesh_TDG2_drhog_rho1_move = disp_oldFD_long_gradmesh_TDG2_drhog_rho1_move.to_numpy()
disp_oldFD_long_gradmesh_TDG2_rho1_bodypresadv = disp_oldFD_long_gradmesh_TDG2_rho1_bodypresadv.to_numpy()
disp_oldFD_long_gradmesh_TDG2_drhog_lagrbuoy = disp_oldFD_long_gradmesh_TDG2_drhog_lagrbuoy.to_numpy()
disp_oldFD_long_gradmesh_TDG2_drhog_norho1_move = disp_oldFD_long_gradmesh_TDG2_drhog_norho1_move.to_numpy()
disp_oldFD_long_gradmesh_TDG2_drhog_advrho1 = disp_oldFD_long_gradmesh_TDG2_drhog_advrho1.to_numpy()
disp_oldFD_long_gradmesh_TDG2_drhog_advrho1_move = disp_oldFD_long_gradmesh_TDG2_drhog_advrho1_move.to_numpy()
disp_oldFD_long_gradmesh_TDG2_rhog_dump75 = disp_oldFD_long_gradmesh_TDG2_rhog_dump75.to_numpy()
disp_oldFD_long_gradmesh_TDG2_rhog_110ka = disp_oldFD_long_gradmesh_TDG2_rhog_110ka.to_numpy()
disp_oldFD_long_gradmesh_TDG2_drhog_110ka = disp_oldFD_long_gradmesh_TDG2_drhog_110ka.to_numpy()
disp_oldFD_long_gradmesh_TDG2_drhog_isostatic = disp_oldFD_long_gradmesh_TDG2_drhog_isostatic.to_numpy()
disp_oldFD_long_gradmesh_TDG2_rhog_isostatic = disp_oldFD_long_gradmesh_TDG2_rhog_isostatic.to_numpy()
disp_oldFD_long_gradmesh_TDG2_drhog_isostatic_nolith = disp_oldFD_long_gradmesh_TDG2_drhog_isostatic_nolith.to_numpy()
disp_oldFD_long_gradmesh_TDG2_rhog_isostatic_nolith = disp_oldFD_long_gradmesh_TDG2_rhog_isostatic_nolith.to_numpy()
#print(np.argmax(disp_oldFD_surfadv_80))

#plt.plot(1e-3*distance_fromcentre, displacement["displacement_vom_array_10years"], 'x', label='160 layers')
#plt.plot(1e-3*distance_fromcentre, displacement["displacement_vom_array_50years"], 'x', label='160 layers')
#plt.plot(1e-3*distance_fromcentre, displacement["displacement_vom_array_100years"], 'x', label='160 layers')

print(displacement[0:])

aspect_displacement = np.loadtxt("/data/free_surface/aspect_box/aspect_fig_3b.csv", delimiter=',')
aspect_displacement2 = np.loadtxt("/data/free_surface/aspect_box/aspect_fig_3b_file.csv", delimiter=',')
aspect_displacement_long = np.loadtxt("/data/free_surface/aspect_box/aspect_fig_4b_file.csv", delimiter=',')
abaqus_displacement_long = np.loadtxt("/data/free_surface/aspect_box/abaqus_picks_fig4b.csv", delimiter=',')
taboo_displacement_long = np.loadtxt("/data/free_surface/aspect_box/taboo_picks_fig4b.csv", delimiter=',')
print(aspect_displacement[:,1])
#plt.plot(displacement[0])

#plt.plot(distance_fromcentre, displacement["displacement_vom_array_200years"], 'x', label='160 layers')
#plt.plot(np.sort(displacement["displacement_vom_array_10years"]), 'x', label='np.sort()')
#plt.plot(disp_2["displacement_vom_array_10years"], 'x', label='VOM input_order')

time = [i*10 for i in range(21)]
time2pt5all = [i*2.5 for i in range(81)]
time2pt5 = [i*2.5 for i in range(len(displacement_zhong[0,1:]))]
time2pt5topid = [i*2.5 for i in range(len(displacement_zhong_topid[0,1:]))]
time2pt5topid_pre = [i*2.5 for i in range(len(displacement_zhong_topid_prestress[0,1:]))]
time2pt5topid_prepos = [i*2.5 for i in range(len(displacement_zhong_topid_prestress_pos[0,1:]))]

time50 = [i*50 for i in range(len(disp_oldFD_long[0,1:]))]
time50rho1g = [i*50 for i in range(len(disp_oldFD_long_rho1g[0,1:]))]
actual_aspect = [-0.06191, -0.1243, -0.1875, -0.2517]

time50gradmesh = [i*50 for i in range(len(disp_oldFD_long_gradmesh[0,1:]))]
time50gradmesh_TDG2 = [i*50 for i in range(len(disp_oldFD_long_gradmesh_TDG2[0,1:]))]
time50gradmesh_TDG2_rho1g = [i*50 for i in range(len(disp_oldFD_long_gradmesh_TDG2_rho1g[0,1:]))]
time50gradmesh_TDG2_strong = [i*50 for i in range(len(disp_oldFD_long_gradmesh_TDG2_strong[0,1:]))]
time50gradmesh_TDG2_from64ka = [64e3 + i*50 for i in range(len(disp_oldFD_long_gradmesh_TDG2_from64ka[0,1:]))]
time50gradmesh_TDG2_strong_gradp = [i*50 for i in range(len(disp_oldFD_long_gradmesh_TDG2_strong_gradp[0,1:]))]
time50gradmesh_TDG2_weak_scale = [i*50 for i in range(len(disp_oldFD_long_gradmesh_TDG2_weak_scale[0,1:]))]
time50gradmesh_TDG2_from75ka_drhog = [75e3 + i*50 for i in range(len(disp_oldFD_long_gradmesh_TDG2_from75_drhog[0,1:]))]
time50gradmesh_TDG2_strong_scaleprevstress = [i*50 for i in range(len(disp_oldFD_long_gradmesh_TDG2_strong_scaleprevstress[0,1:]))]
time50gradmesh_TDG2_drhog = [i*50 for i in range(len(disp_oldFD_long_gradmesh_TDG2_drhog[0,1:]))]
time50gradmesh_TDG2_drhog_rho1g = [i*50 for i in range(len(disp_oldFD_long_gradmesh_TDG2_drhog_rho1g[0,1:]))]
time50gradmesh_TDG2_drhog_rho1g_strong = [i*50 for i in range(len(disp_oldFD_long_gradmesh_TDG2_drhog_rho1g_strong[0,1:]))]
time50gradmesh_TDG2_nodrhog = [i*50 for i in range(len(disp_oldFD_long_gradmesh_TDG2_nodrhog[0,1:]))]
time50gradmesh_TDG2_bodypresadv = [i*50 for i in range(len(disp_oldFD_long_gradmesh_TDG2_rho1_bodypresadv[0,1:]))]
time50gradmesh_TDG2_lagrbuoy = [i*50 for i in range(len(disp_oldFD_long_gradmesh_TDG2_drhog_lagrbuoy[0,1:]))]
time50gradmesh_TDG2_drho_norho1_move = [i*50 for i in range(len(disp_oldFD_long_gradmesh_TDG2_drhog_norho1_move[0,1:]))]
time50gradmesh_TDG2_drho_advrho1 = [i*50 for i in range(len(disp_oldFD_long_gradmesh_TDG2_drhog_advrho1[0,1:]))]
time50gradmesh_TDG2_drho_advrho1_move = [i*50 for i in range(len(disp_oldFD_long_gradmesh_TDG2_drhog_advrho1_move[0,1:]))]
time50gradmesh_TDG2_rho_dump75 = [75e3 + i*50 for i in range(len(disp_oldFD_long_gradmesh_TDG2_rhog_dump75[0,1:]))]
time50gradmesh_TDG2_rho_110ka = [110e3 + i*50 for i in range(len(disp_oldFD_long_gradmesh_TDG2_rhog_110ka[0,1:]))]
time50gradmesh_TDG2_drho_110ka = [110e3 + i*50 for i in range(len(disp_oldFD_long_gradmesh_TDG2_drhog_110ka[0,1:]))]
time50gradmesh_TDG2_drho_iso = [i*50 for i in range(len(disp_oldFD_long_gradmesh_TDG2_drhog_isostatic[0,1:]))]
time50gradmesh_TDG2_rho_iso = [i*50 for i in range(len(disp_oldFD_long_gradmesh_TDG2_rhog_isostatic[0,1:]))]
time50gradmesh_TDG2_drho_iso_nolith = [i*50 for i in range(len(disp_oldFD_long_gradmesh_TDG2_drhog_isostatic_nolith[0,1:]))]
time50gradmesh_TDG2_rho_iso_nolith = [i*50 for i in range(len(disp_oldFD_long_gradmesh_TDG2_rhog_isostatic_nolith[0,1:]))]

#plt.plot(time, displacement[0,1:], 'x', label='nz 160')
#plt.plot(time, displacement_40[0,1:], 'x', label='nz 40')
#plt.plot(time2pt5, displacement_zhong[0,1:], '-', label='zhong')
#plt.plot(time2pt5topid, displacement_zhong_topid[0,1:], 'x', label='zhong top id')
#plt.plot(time2pt5topid_pre, displacement_zhong_topid_prestress[0,1:], 'x', label='zhong top id prestress')
#plt.plot(time2pt5topid_prepos, displacement_zhong_topid_prestress_pos[0,1:], 'x', label='zhong top id prestress positive')
#plt.plot(time2pt5all, displacement_zhong_topid_prestress_pos_nodrhog[0,1:], 'x-', label='zhong top id prestress positive no delta rhog')
#plt.plot(time2pt5all, displacement_zhong_topid_prestress_pos_nodrhog_80[0,1:], 'x-', label='zhong top id prestress positive no delta rhog, 80 layers')
#plt.plot(time2pt5all, displacement_zhong_topid_prestress_pos_nodrhog_160[0,1:], 'x-', label='zhong top id prestress positive no delta rhog, 160 layers')
#plt.plot(time2pt5all, displacement_zhong_topid_nodrhog[0,1:], 'x-', label='zhong top id no delta rhog, 40 layers')
#plt.plot(time2pt5all, displacement_zhong_topid_nodrhog_80[0,1:], 'x-', label='zhong top id no delta rhog, 80 layers')



fig, ax = plt.subplots(1, 1)
#plt.plot(200, -0.774224, 'v', label='old FD with surface id off')
#plt.plot(200, -0.75205, 'v', label='old FD with surface id on')
#plt.plot(time2pt5all, displacement_zhong_topid_prestress_pos_nodrhog_160[71,1:], 'x-', label='zhong top id prestress positive no delta rhog, 160 layers')
#plt.plot(time[:12], displacement_rhog[0,1:], 'x', label='delta rhog')
#plt.plot(aspect_displacement[:,0],aspect_displacement[:,1], 'x', label='aspect digitised')
ax.plot(aspect_displacement2[:,0],aspect_displacement2[:,1], 'x', label='Aspect')
#ax.plot(time, disp_oldFD_surfadv, 'x', label='Firedrake')
ax.plot(time2pt5all, disp_oldFD_surfadv_80[index, 1:], 'x', label='Firedrake')
ax.plot(time2pt5all, disp_oldFD_surfadv_80_check[index_check, 1:], 'x', label='Firedrake check')
#plt.plot(100, -0.6564, 'x')

#ax.set_ylim([-0.8, 0.1])
ax.set_xlabel('Time (years)')
ax.set_ylabel('Maximum vertical displacement (m)')
ax.grid(True)
ax.legend()
#fig.isavefig('17.10.23_oldFD_withsurfaceadv_vsaspect_max_justFD80layers.png')


fig, ax = plt.subplots(1, 1, figsize=(20, 15))

#plt.plot(200, -0.774224, 'v', label='old FD with surface id off')
#plt.plot(200, -0.75205, 'v', label='old FD with surface id on')
#plt.plot(time2pt5all, displacement_zhong_topid_prestress_pos_nodrhog_160[71,1:], 'x-', label='zhong top id prestress positive no delta rhog, 160 layers')
#plt.plot(time[:12], displacement_rhog[0,1:], 'x', label='delta rhog')
#plt.plot(aspect_displacement[:,0],aspect_displacement[:,1], 'x', label='aspect digitised')
ax.plot(abaqus_displacement_long[:,0]*1e3,abaqus_displacement_long[:,1], 'x-', label='Abaqus')
ax.plot(taboo_displacement_long[:,0]*1e3,taboo_displacement_long[:,1], 'x-', label='Taboo')

# use this for aspect long..?
ax.plot(aspect_displacement_long[:,0],aspect_displacement_long[:,1], 'g-', label='Aspect')


#ax.plot(time, disp_oldFD_surfadv, 'x', label='Firedrake')
#ax.plot(time50, disp_oldFD_long[index_long, 1:], 'x', label='Firedrake')
#ax.plot(time50rho1g, disp_oldFD_long_rho1g[index_long_rho1g, 1:], 'x', label='Firedrake rho1g')
#ax.plot(time50gradmesh, disp_oldFD_long_gradmesh[index_long_gradmesh, 1:], 'x', label='Firedrake grad mesh')
#ax.plot(time50gradmesh_TDG2, disp_oldFD_long_gradmesh_TDG2[index_long_gradmesh_TDG2, 1:], 'x-', label='Firedrake up to 75ka (original)')
#ax.plot(time50gradmesh_TDG2_rho1g, disp_oldFD_long_gradmesh_TDG2_rho1g[index_long_gradmesh_TDG2_rho1g, 1:], '-', label='Firedrake with rho1g')
#ax.plot(time50gradmesh_TDG2_weak_scale, disp_oldFD_long_gradmesh_TDG2_weak_scale[index_long_gradmesh_TDG2_weak_scale, 1:], '-x', label='Firedrake grad mesh TDG2 + weak bc (bad scaling)')
#ax.plot(time50gradmesh_TDG2_strong, disp_oldFD_long_gradmesh_TDG2_strong[index_long_gradmesh_TDG2_strong, 1:], 'x', label='Firedrake grad mesh TDG2 + strong bc (bad scaling)')
#ax.plot(time50gradmesh_TDG2_from64ka, disp_oldFD_long_gradmesh_TDG2_from64ka[index_long_gradmesh_TDG2, 1:], 'x', label='Firedrake grad mesh TDG2 from 64ka') # use TD2 index to line up exactly... i guess same parallel decomposition...? if you use actual min at pick up it is slightly offset because of the kink at the boundary...
#ax.plot(time50gradmesh_TDG2_strong_gradp, disp_oldFD_long_gradmesh_TDG2_strong_gradp[index_long_gradmesh_TDG2_strong, 1:], 'x', label='Firedrake grad mesh TDG2 + strong bc (bad scaling with gradp)')
#ax.plot(time50gradmesh_TDG2_from75ka_drhog, disp_oldFD_long_gradmesh_TDG2_from75_drhog[index_long_gradmesh_TDG2, 1:], 'x', label='Firedrake grad mesh TDG2 from 75ka and drhog') # use TD2 index to line up exactly... i guess same parallel decomposition...? if you use actual min at pick up it is slightly offset because of the kink at the boundary...
#ax.plot(time50gradmesh_TDG2_strong_scaleprevstress, disp_oldFD_long_gradmesh_TDG2_strong_scaleprevstress[index_long_gradmesh_TDG2_strong_scaleprevstress, 1:], 'o', label='Firedrake grad mesh TDG2 + strong bc (good scaling)')
#ax.plot(time50gradmesh_TDG2_drhog_rho1g, disp_oldFD_long_gradmesh_TDG2_drhog_rho1g[index_long_gradmesh_TDG2_drhog_rho1g, 1:], '-', label='Firedrake with both rho1g and delta rhog (weak)')
#ax.plot(time50gradmesh_TDG2_rho_dump75, disp_oldFD_long_gradmesh_TDG2_rhog_dump75[index_long_gradmesh_TDG2, 1:], 'x-', label='from checkpoint 75ka')
#ax.plot(time50gradmesh_TDG2_nodrhog, disp_oldFD_long_gradmesh_TDG2_nodrhog[index_long_gradmesh_TDG2_nodrhog, 1:], '-', label='Prestress: rho, no rho1',  alpha=1)
#ax.plot(time50gradmesh_TDG2_drhog, disp_oldFD_long_gradmesh_TDG2_drhog[index_long_gradmesh_TDG2_drhog, 1:], '-', label='pre Hobart, Prestress: Delta rho, no rho1', alpha=1)
#ax.plot(time50gradmesh_TDG2_rho1g, disp_oldFD_long_gradmesh_TDG2_rho1g[index_long_gradmesh_TDG2_rho1g, 1:], '-', label='pre Hobart, Prestress: rho, rho1', alpha=1)
#ax.plot(time50gradmesh_TDG2_drhog_rho1g_strong, disp_oldFD_long_gradmesh_TDG2_drhog_rho1g_strong[index_long_gradmesh_TDG2_drhog_rho1g_strong, 1:], '-', color='black', label='Hobart, Prestress: Delta rho, rho1')
#ax.plot(110e3, disp_oldFD_long_gradmesh_TDG2_drhog_rho1g_strong[index_long_gradmesh_TDG2_drhog_rho1g_strong, 1+round(110e3/50)], 'ro', markersize=10, mew=2)
#plt.plot(100, -0.6564, 'x')
#ax.plot(time50gradmesh_TDG2_drhog_rho1g_strong, disp_oldFD_long_gradmesh_TDG2_zerodrhog_norho1[index_long_gradmesh_TDG2_zerodrhog_norho1, 1:], '-', label='Post Hobart, Prestress: zero, no rho1', alpha=1)
#ax.plot(time50gradmesh_TDG2_drhog_rho1g_strong, disp_oldFD_long_gradmesh_TDG2_zerodrhog_rho1[index_long_gradmesh_TDG2_zerodrhog_rho1, 1:], '-', label='Post Hobart, Prestress: zero, rho1',alpha=1)
#ax.plot(time50gradmesh_TDG2_bodypresadv, disp_oldFD_long_gradmesh_TDG2_rho1_bodypresadv[index_long_gradmesh_TDG2_rho1_bodypresadv, 1:], '-', label='Post Hobart, Prestress: rho (body term), rho1', alpha=1)
#ax.plot(time50gradmesh_TDG2_lagrbuoy, disp_oldFD_long_gradmesh_TDG2_drhog_lagrbuoy[index_long_gradmesh_TDG2_drhog_lagrbuoy, 1:], '-', label='G-ADOPT  body drhog, lagrangian buoyancy ')
#ax.plot(time50gradmesh_TDG2_drhog_rho1g_strong, disp_oldFD_long_gradmesh_TDG2_drhog_rho1_move[index_long_gradmesh_TDG2_drhog_move, 1:], 'x', label='Post Hobart, Prestress: Delta rho, rho1, move')
#ax.plot(time50gradmesh_TDG2_drho_norho1_move, disp_oldFD_long_gradmesh_TDG2_drhog_norho1_move[index_long_gradmesh_TDG2_drhog_norho1_move, 1:], 'x', label='Post Hobart, Prestress: Delta drho, no rho1, move')
#ax.plot(time50gradmesh_TDG2_drho_advrho1, disp_oldFD_long_gradmesh_TDG2_drhog_advrho1[index_long_gradmesh_TDG2_drhog_advrho1, 1:], '-', label='Post Hobart, Prestress: Delta drho, advect rho1')
#ax.plot(time50gradmesh_TDG2_drho_advrho1_move, disp_oldFD_long_gradmesh_TDG2_drhog_advrho1_move[index_long_gradmesh_TDG2_drhog_advrho1_move, 1:], '-', label='Post Hobart, Prestress: Delta drho, advect rho1, move')
#ax.plot(time50gradmesh_TDG2_rho_dump75, disp_oldFD_long_gradmesh_TDG2_rhog_dump75[index_long_gradmesh_TDG2_rhog_dump75, 1:], 'x-', label='Post Hobart, Prestress: rho, pickup 75ka')
#ax.plot(time50gradmesh_TDG2_rho_dump75, disp_oldFD_long_gradmesh_TDG2_rhog_dump75[index_long_gradmesh_TDG2, 1:], 'x-', label='from checkpoint 75ka')
#ax.plot(time50gradmesh_TDG2_rho_110ka, disp_oldFD_long_gradmesh_TDG2_rhog_110ka[index_long_gradmesh_TDG2_rhog_110ka, 1:], 'x-', label='(weak) rhog from 110ka')
#ax.plot(time50gradmesh_TDG2_drho_110ka, disp_oldFD_long_gradmesh_TDG2_drhog_110ka[index_long_gradmesh_TDG2_drhog_rho1g_strong, 1:], 'x-', label='(strong) drhog from 110ka')
#ax.plot(time50gradmesh_TDG2_drho_iso, disp_oldFD_long_gradmesh_TDG2_drhog_isostatic[index_long_gradmesh_TDG2_drhog_iso, 1:], 'x-', label='(strong) drhog from rest continue to isostatic')
#ax.plot(time50gradmesh_TDG2_rho_iso, disp_oldFD_long_gradmesh_TDG2_rhog_isostatic[index_long_gradmesh_TDG2_rhog_iso, 1:], 'x-', label='(strong) rhog from rest continue to isostatic')
#ax.plot(time50gradmesh_TDG2_drhog_rho1g_strong, disp_oldFD_long_gradmesh_TDG2_drhog_rho1g_strong[index_long_gradmesh_TDG2_drhog_rho1g_strong, 1:], '-', color='black', label='Hobart, Prestress: Delta rho, rho1')
#ax.plot(time50gradmesh_TDG2_drho_iso_nolith, disp_oldFD_long_gradmesh_TDG2_drhog_isostatic_nolith[index_long_gradmesh_TDG2_drhog_iso_nolith, 1:], '-',color='orange', label='(strong) drhog from rest continue to isostatic, no lithosphere')
#ax.plot(time50gradmesh_TDG2_rho_iso_nolith, disp_oldFD_long_gradmesh_TDG2_rhog_isostatic_nolith[index_long_gradmesh_TDG2_rhog_iso_nolith, 1:], 'x-', label='(strong) rhog from rest continue to isostatic, no lithosphere')
#ax.plot(disp_oldFD_long_gradmesh_TDG2_rhog_isostatic_nolith_func[0], disp_oldFD_long_gradmesh_TDG2_rhog_isostatic_nolith_func[1][disp_oldFD_long_gradmesh_TDG2_rhog_isostatic_nolith_func[2], 1:], 'o-', label='(strong) rhog from rest continue to isostatic, no lithosphere, function')
#ax.plot(disp_drhog_iso_nolith_100ka[0], disp_drhog_iso_nolith_100ka[1][disp_drhog_iso_nolith_100ka[2], 1:], '-',color='orange')
#ax.plot(disp_TP1[0], disp_TP1[1][disp_TP1[2], 1:], '-x',color='purple', label='TP1')
#font = {'size': 22}

#ax.plot(disp_2d_old[0], disp_2d_old[1][disp_2d_old[2], 1:], '-x', markevery=10, label='2d old viscoelastic branch, old Firedrake (GADI)')
#ax.plot(disp_2d_old_newFD[0], disp_2d_old_newFD[1][disp_2d_old_newFD[2], 1:], '-', label='2d old, new Firedrake')
#ax.plot(disp_2d_old_newFD_nofs[0], disp_2d_old_newFD_nofs[1][disp_2d_old_newFD_nofs[2], 1:], '-', label='2d old, new Firedrake, no free surface')
#ax.plot(disp_2d_new[0], disp_2d_new[1][disp_2d_new[2], 1:], '-x', label='2d new, minus ice load ')
#ax.plot(disp_2d_new_zerodens[0], disp_2d_new_zerodens[1][disp_2d_new_zerodens[2], 1:], '-', label='2d new, minus ice load, no exterior density')
#ax.plot(disp_2d_new_fs[0], disp_2d_new_fs[1][disp_2d_new_fs[2], 1:], '-',color='black', label='2d new, minus ice load,  free surface')
#ax.plot(disp_2d_new_fs_exd[0], disp_2d_new_fs_exd[1][disp_2d_new_fs_exd[2], 1:], '-', label='2d new, minus ice load,  free surface, exterior density')

# Checking CI change due to tanh dx/self.dx 18.03.24
#ax.plot(disp_2d_new_MPInodes_180324old[:, 0], disp_2d_new_MPInodes_180324old[:, 1], '-o', markevery=20, label='2d original commit')
#ax.plot(disp_2d_new_MPInodes_180324old_meshres[:, 0], disp_2d_new_MPInodes_180324old_meshres[:, 1], '-o', markevery=20, label='2d mesh res commit')
#ax.plot(disp_2d_new_MPInodes_180324old_meshresdisc5000[:, 0], disp_2d_new_MPInodes_180324old_meshresdisc5000[:, 1], '-o', markevery=20, label='2d mesh res commiti disc 5km')
#ax.plot(disp_2d_new_MPInodes_190324newdisc5000[:, 0], disp_2d_new_MPInodes_190324newdisc5000[:, 1], '-x', markevery=30, label='2d mesh up-to-date disc 5km')


# plot with/without low viscosity (instantaneous ice load) for 100 steps
#ax.plot(disp_2d_instantload[:, 0], disp_2d_instantload[:, 1], '-o', markevery=20, label='2d instantaneous load')
#ax.plot(disp_2d_instantload_lowvisc[:, 0], disp_2d_instantload_lowvisc[:, 1], '-o', markevery=20, label='2d instantaneous load, low viscosity')


# plot optimised results iterations
#ax.plot(disp_2d_instantload_dx5_nz160squash[:, 0], disp_2d_instantload_dx5_nz160squash[:, 1], '-o', markevery=1, label='Initial, layered viscosity')
#ax.plot(disp_2d_instantload_lowvisc_dx5_nz160squash[:, 0], disp_2d_instantload_lowvisc_dx5_nz160squash[:, 1], '-o', markevery=1, label='Target, low viscosity region')

#optimised_viscosity_displacements = [disp_2d_instantload_optvisc_lb1emin4_it1,
#        disp_2d_instantload_optvisc_lb1emin4_it2,
#        disp_2d_instantload_optvisc_lb1emin4_it3,
#        disp_2d_instantload_optvisc_lb1emin4_it4,
#        disp_2d_instantload_optvisc_lb1emin4_it5,
#        disp_2d_instantload_optvisc_lb1emin4_it6,
#        disp_2d_instantload_optvisc_lb1emin4_it7,
#        disp_2d_instantload_optvisc_lb1emin4_it8,
#        disp_2d_instantload_optvisc_lb1emin4_it9,
#        disp_2d_instantload_optvisc_lb1emin4_it10,
#        disp_2d_instantload_optvisc_lb1emin4_it11]

#iteration =11
#for i in range(iteration):
#    if i == iteration-1:
#        alpha = 1
#    else:
#        alpha = 0.2
#    ax.plot(optimised_viscosity_displacements[i][:, 0], optimised_viscosity_displacements[i][:, 1], '-o', markevery=1, color='black', alpha=alpha, label=f'Optimised viscosity, iteration {i+1}')



#ax.plot(disp_2d_instantload_optvisc_lb1emin4[:, 0], disp_2d_instantload_optvisc_lb1emin4[:, 1], '-o', markevery=1, color='black', label='Optimised viscosity, iteration 11')
#ax.plot(disp_2d_instantload_optvisc_lb1emin4_it2[:, 0], disp_2d_instantload_optvisc_lb1emin4_it2[:, 1], '-o', markevery=1, color='black', alpha=0.2, label='Optimised viscosity, iteration 2')
#ax.plot(disp_2d_instantload_optvisc_lb1emin5[:, 0], disp_2d_instantload_optvisc_lb1emin5[:, 1], '-o', markevery=1, label='Optimised viscosity, lower bound = 1e-5')
#ax.plot(disp_2d_instantload_optvisc_lb1emin5_it1[:, 0], disp_2d_instantload_optvisc_lb1emin5_it1[:, 1], '-o',color='red', markevery=1, label='Optimised viscosity, lower bound = 1e-5, iteration 1')
#ax.plot(disp_3d_new_gadi[:, 0], disp_3d_new_gadi[:, 1], 'o', markevery=10, label='3d new viscoelastic branch, new Firedrake')
#

####
# plot 2d vertical resolution conditional vs tanh
#ax.plot(disp_2d_nz40_conditional[:, 0], disp_2d_nz40_conditional[:, 1], '--', color='red', markevery=20, label='nz = 40, conditional')
#ax.plot(disp_2d_nz80_conditional[:, 0], disp_2d_nz80_conditional[:, 1], '--',color='blue', markevery=20, label='nz = 80, conditional')
#ax.plot(disp_2d_nz160_conditional[:, 0], disp_2d_nz160_conditional[:, 1], '--',color='orange', markevery=20, label='nz = 160, conditional')
#ax.plot(disp_2d_nz320_conditional[:, 0], disp_2d_nz320_conditional[:, 1], '--',color='black', markevery=20, label='nz = 320, conditional')

#ax.plot(disp_2d_nz40_tanh[:, 0], disp_2d_nz40_tanh[:, 1], 'x', markevery=20,color='red', label='nz = 40, tanh (width = 10 km)')
#ax.plot(disp_2d_nz80_tanh[:, 0], disp_2d_nz80_tanh[:, 1], 'x', markevery=20,color='blue', label='nz = 80, tanh (width = 10 km)')
#ax.plot(disp_2d_nz160_tanh[:, 0], disp_2d_nz160_tanh[:, 1], 'x', markevery=20,color='orange', label='nz = 160, tanh (width = 10 km)')

#ax.plot(disp_2d_nz40_tanh_5km[:, 0], disp_2d_nz40_tanh_5km[:, 1], 's', markevery=20,color='red', label='nz = 40, tanh (width = 5 km)')
#ax.plot(disp_2d_nz80_tanh_5km[:, 0], disp_2d_nz80_tanh_5km[:, 1], 's', markevery=20,color='blue', label='nz = 80, tanh (width = 5 km)')
#ax.plot(disp_2d_nz160_tanh_5km[:, 0], disp_2d_nz160_tanh_5km[:, 1], 's', markevery=20,color='orange', label='nz = 160, tanh (width = 5 km)')

#ax.plot(disp_2d_nz40_tanh_2pt5km[:, 0], disp_2d_nz40_tanh_2pt5km[:, 1], '^', markevery=20,color='red', label='nz = 40, tanh (width = 2.5 km)')
#ax.plot(disp_2d_nz80_tanh_2pt5km[:, 0], disp_2d_nz80_tanh_2pt5km[:, 1], '^', markevery=20,color='blue', label='nz = 80, tanh (width = 2.5 km)')
#ax.plot(disp_2d_nz160_tanh_2pt5km[:, 0], disp_2d_nz160_tanh_2pt5km[:, 1], '^', markevery=20,color='orange', label='nz = 160, tanh (width = 2.5 km)')
#ax.plot(disp_2d_nz320_tanh_2pt5km[:, 0], disp_2d_nz320_tanh_2pt5km[:, 1], '^', markevery=20,color='black', label='nz = 320, tanh (width = 2.5 km)')

#ax.plot(disp_2d_nz40_tanh_1km[:, 0], disp_2d_nz40_tanh_1km[:, 1], 'P', markevery=20,color='red', label='nz = 40, tanh (width = 1 km)')
#ax.plot(disp_2d_nz80_tanh_1km[:, 0], disp_2d_nz80_tanh_1km[:, 1], 'P', markevery=20,color='blue', label='nz = 80, tanh (width = 1 km)')
#ax.plot(disp_2d_nz160_tanh_1km[:, 0], disp_2d_nz160_tanh_1km[:, 1], 'P', markevery=20,color='orange', label='nz = 160, tanh (width = 1 km)')
#ax.plot(disp_2d_nz320_tanh_1km[:, 0], disp_2d_nz320_tanh_1km[:, 1], 'P', markevery=20,color='black', label='nz = 320, tanh (width = 1 km)')

#ax.plot(disp_2d_nz40_tanh_500m[:, 0], disp_2d_nz40_tanh_500m[:, 1], 'D', markevery=20,color='red', label='nz = 40, tanh (width = 500 m)')
#ax.plot(disp_2d_nz80_tanh_500m[:, 0], disp_2d_nz80_tanh_500m[:, 1], 'D', markevery=20,color='blue', label='nz = 80, tanh (width = 500 m)')
#ax.plot(disp_2d_nz160_tanh_500m[:, 0], disp_2d_nz160_tanh_500m[:, 1], 'D', markevery=20,color='orange', label='nz = 160, tanh (width = 500 m)')
#ax.plot(disp_2d_nz320_tanh_500m[:, 0], disp_2d_nz320_tanh_500m[:, 1], 'D', markevery=20,color='black', label='nz = 320, tanh (width = 500 m)')
#####
#ax.plot(disp_3d_new_gadi_inherit[:, 0], disp_3d_new_gadi_inherit[:, 1], 'x', markevery=20, label='3d new viscoelastic branch, new Firedrake, inheritance')
# Plot resolution tests

# Structured surface mesh
#ax.plot(disp_3d_struc_dx50_nz80_dt50[:, 0], disp_3d_struc_dx50_nz80_dt50[:, 1], 'x', markevery=20, label='3d dx = 50 km (structured), nz = 80, dt = 50 years')
#ax.plot(disp_3d_struc_dx25_nz80_dt50[:, 0], disp_3d_struc_dx25_nz80_dt50[:, 1], 'x', markevery=20, label='3d dx = 25 km (structured), nz = 80, dt = 50 years')
#ax.plot(disp_3d_struc_dx12_nz80_dt50[:, 0], disp_3d_struc_dx12_nz80_dt50[:, 1], 'x', markevery=20, label='3d dx = 12.5 km (structured), nz = 80, dt = 50 years')
#ax.plot(disp_3d_struc_dx50_nz80_dt50_sharpice[:, 0], disp_3d_struc_dx50_nz80_dt50_sharpice[:, 1], 'x', markevery=20, label='3d dx = 50 km (structured), sharper ice transition, nz = 80, dt = 50 years')

# Refined surface
#ax.plot(disp_3d_dx20_nz80_dt50[:, 0], disp_3d_dx20_nz80_dt50[:, 1], 'x', markevery=20, label='3d dx = 20 km (refined), nz = 80, dt = 50 years')
#ax.plot(disp_3d_dx10_nz80_dt50[:, 0], disp_3d_dx10_nz80_dt50[:, 1], 'x', markevery=20, label='3d dx = 10 km (refined), nz = 80, dt = 50 years')
#ax.plot(disp_3d_dx5_nz80_dt50[:, 0], disp_3d_dx5_nz80_dt50[:, 1], 'x', markevery=20, label='3d dx = 5 km (refined), nz = 80, dt = 50 years (default)')

# Vertical resolution
#ax.plot(disp_3d_dx5_nz20_dt50[:, 0], disp_3d_dx5_nz20_dt50[:, 1], 'o', markevery=20, color='green', label='nz = 20, squashed')
#ax.plot(disp_3d_dx5_nz40_dt50[:, 0], disp_3d_dx5_nz40_dt50[:, 1], 'o', markevery=20, color='blue', label='nz = 40, squashed')
#ax.plot(disp_3d_dx5_nz80_dt50[:, 0], disp_3d_dx5_nz80_dt50[:, 1], 'o', markevery=20, color='black', label='nz, squashed')
#ax.plot(disp_3d_dx5_nz160_dt50[:, 0], disp_3d_dx5_nz160_dt50[:, 1], 'o', color='red',markevery=20, label='nz = 160, squashed')
#ax.plot(disp_3d_dx5_nz160_dt50_50ka[:, 0], disp_3d_dx5_nz160_dt50_50ka[:, 1], 'o', color='red', markevery=20,)

# Vertical 3d tanh 5km width
#ax.plot(disp_3d_nz40_tanh5000[:, 0], disp_3d_nz40_tanh5000[:, 1], 'x', markevery=20, color='blue', label='3d dx = 5 km (refined), nz = 40, dt = 50 years, tanh width = 5 km')
#ax.plot(disp_3d_nz80_tanh5000[:, 0], disp_3d_nz80_tanh5000[:, 1], 'x', markevery=20, color='black', label='3d dx = 5 km (refined), nz = 80, dt = 50 years, tanh width = 5 km')
#ax.plot(disp_3d_nz160_tanh5000[:, 0], disp_3d_nz160_tanh5000[:, 1], 'x', color='red',markevery=20, label='3d dx = 5 km (refined), nz = 160, dt = 50 years, tanh width = 5 km')

# Vertical 3d tanh 10km width
#ax.plot(disp_3d_nz40_tanh10000[:, 0], disp_3d_nz40_tanh10000[:, 1], '+', markevery=20, color='blue', label='3d dx = 5 km (refined), nz = 40, dt = 50 years, tanh width = 10 km')
#ax.plot(disp_3d_nz80_tanh10000[:, 0], disp_3d_nz80_tanh10000[:, 1], '+', markevery=20, color='black', label='3d dx = 5 km (refined), nz = 80, dt = 50 years, tanh width = 10 km')
#ax.plot(disp_3d_nz160_tanh10000[:, 0], disp_3d_nz160_tanh10000[:, 1], '+', color='red',markevery=20, label='3d dx = 5 km (refined), nz = 160, dt = 50 years, tanh width = 10 km')

# Vertical 3d tanh check no tanh nov 24
#ax.plot(disp_3d_nz640_check[:, 0], disp_3d_nz640_check[:, 1], '+', color='blue',markevery=20, label='3d dx = 5 km (refined), nz = 640, dt = 50 years, tanh width = 0 km')
#ax.plot(disp_3d_nz320_check[:, 0], disp_3d_nz320_check[:, 1], '+', color='green',markevery=20, label='3d dx = 5 km (refined), nz = 320, dt = 50 years, tanh width = 0 km')
#ax.plot(disp_3d_nz160_check[:, 0], disp_3d_nz160_check[:, 1], '+', color='orange',markevery=20, label='3d dx = 5 km (refined), nz = 160, dt = 50 years, tanh width = 0 km')
#ax.plot(disp_3d_nz80_check[:, 0], disp_3d_nz80_check[:, 1], '+', color='red',markevery=20, label='3d dx = 5 km (refined), nz = 80, dt = 50 years, tanh width = 0 km')
#ax.plot(disp_3d_nz40_check[:, 0], disp_3d_nz40_check[:, 1], '+', color='black',markevery=20, label='3d dx = 5 km (refined), nz = 40, dt = 50 years, tanh width = 0 km')
#ax.plot(disp_3d_nz20_check[:, 0], disp_3d_nz20_check[:, 1], '+', color='purple',markevery=20, label='3d dx = 5 km (refined), nz = 20, dt = 50 years, tanh width = 0 km')
#ax.plot(disp_3d_nz80_check_squash[:, 0], disp_3d_nz80_check_squash[:, 1], 'x', color='red',markevery=20, label='3d dx = 5 km (refined), nz = 80, dt = 50 years, tanh width = 0 km, squash mesh')

# DG0 with mesh cells aligned with profile jumps dec 24
#ax.plot(disp_3d_DG0_nz5[:, 0], disp_3d_DG0_nz5[:, 1], '^', color='green',markevery=20, label='DG cells per layer 5')
#ax.plot(disp_3d_DG0_nz8[:, 0], disp_3d_DG0_nz8[:, 1], '^', color='green',markevery=20, label='3d dx = 5 km (refined), DG cells per layer 8, dt = 50 years, tanh width = 0 km')
#ax.plot(disp_3d_DG0_nz10[:, 0], disp_3d_DG0_nz10[:, 1], '^', color='blue',markevery=20, label='DG cells per layer 10')
#ax.plot(disp_3d_DG0_nz20[:, 0], disp_3d_DG0_nz20[:, 1], '^', color='black',markevery=20, label='DG cells per layer 20')
#ax.plot(disp_3d_DG0_nz40[:, 0], disp_3d_DG0_nz40[:, 1], '^', color='red',markevery=20, label='DG cells per layer 40')

# P1 centred with mesh cells aligned with profile jumps dec 24
#ax.plot(disp_3d_P1_nz5[:, 0], disp_3d_P1_nz5[:, 1], 'v', color='green',markevery=20, label='P1 cells per layer 5')
#ax.plot(disp_3d_P1_nz8[:, 0], disp_3d_P1_nz8[:, 1], 'v', color='green',markevery=20, label='3d dx = 5 km (refined), P1 cells per layer 8, dt = 50 years, tanh width = 0 km')
#ax.plot(disp_3d_P1_nz10[:, 0], disp_3d_P1_nz10[:, 1], 'v', color='blue',markevery=20, label='P1 cells per layer 10')
#ax.plot(disp_3d_P1_nz20[:, 0], disp_3d_P1_nz20[:, 1], 'v', color='black',markevery=20, label='P1 cells per layer 20')
#ax.plot(disp_3d_P1_nz40[:, 0], disp_3d_P1_nz40[:, 1], 'v', color='red',markevery=20, label='P1 cells per layer 40')

# DG0 aligned with profile jumps dec 24 icetanh 1km
#ax.plot(disp_3d_DGO_nz5_icetanh1km_dt800[:, 0], disp_3d_DGO_nz5_icetanh1km_dt800[:, 1], 'x', color='purple',markevery=1, label='3d dx = 5 km (refined), DG0 cells per layer 5, dt = 800 years, tanh width = 0 km, icetanh 1km')
#ax.plot(disp_3d_DGO_nz5_icetanh2km_dt800[:, 0], disp_3d_DGO_nz5_icetanh2km_dt800[:, 1], 'x', color='orange',markevery=1, label='3d dx = 5 km (refined), DG0 cells per layer 5, dt = 800 years, tanh width = 0 km, icetanh 1km')
#ax.plot(disp_3d_DGO_nz5_icetanh15km_dt800[:, 0], disp_3d_DGO_nz5_icetanh15km_dt800[:, 1], 'x', color='red',markevery=1, label='3d dx = 5 km (refined), DG0 cells per layer 5, dt = 800 years, tanh width = 0 km, icetanh 15km')
#ax.plot(disp_3d_DGO_nz5_icetanh15km_dt400[:, 0], disp_3d_DGO_nz5_icetanh15km_dt400[:, 1], 'x', color='blue',markevery=1, label='3d dx = 5 km (refined), DG0 cells per layer 5, dt = 400 years, tanh width = 0 km, icetanh 15km')

# P1 centred profile dec 24 g = 9.815
#ax.plot(disp_3d_P1_nz20_g[:, 0], disp_3d_P1_nz20_g[:, 1], '--', color='orange', label='3d dx = 5 km (refined), P1 cells per layer 20, dt = 50 years, tanh width = 0 km, modified g=9.815')
#ax.plot(disp_3d_P1_nz20_g_nofsrho1[:, 0], disp_3d_P1_nz20_g_nofsrho1[:, 1], '--', color='green', label='3d dx = 5 km (refined), P1 cells per layer 20, dt = 50 years, tanh width = 0 km, modifid g =9.815')
#ax.plot(disp_3d_P1_nz20_g_nofsrho1_norho1[:, 0], disp_3d_P1_nz20_g_nofsrho1_norho1[:, 1], '--', color='red', label='3d dx = 5 km (refined), P1 cells per layer 20, dt = 50 years, tanh width = 0 km, modifid g =9.815, norho1')

# DG0 aligned with profile jumps dec 24 rho1 advection
#ax.plot(disp_3d_DG0_nz5_rho1adv[:, 0], disp_3d_DG0_nz5_rho1adv[:, 1], '-o', color='green',markevery=1, label='3d dx = 5 km (refined), DG0 cells per layer 5, dt = 800 years, rho1 advection')
#ax.plot(disp_3d_DG0_nz10_rho1adv[:, 0], disp_3d_DG0_nz10_rho1adv[:, 1], '-o', color='blue',markevery=1, label='3d dx = 5 km (refined), DG0 cells per layer 10, dt = 800 years, rho1 advection')
#ax.plot(disp_3d_DG0_nz20_rho1adv[:, 0], disp_3d_DG0_nz20_rho1adv[:, 1], '-o', color='black',markevery=1, label='3d dx = 5 km (refined), DG0 cells per layer 20, dt = 800 years, rho1 advection')

#ax.plot(disp_3d_DG0_nz5_rho1adv_bc0[:, 0], disp_3d_DG0_nz5_rho1adv_bc0[:, 1], 'x', color='green',markevery=1, label='3d dx = 5 km (refined), DG0 cells per layer 5, dt = 800 years, rho1 advection, rhobc 0')
#ax.plot(disp_3d_DG0_nz5_rho1adv_bcdiff[:, 0], disp_3d_DG0_nz5_rho1adv_bcdiff[:, 1], '*', color='green',markevery=1, label='3d dx = 5 km (refined), DG0 cells per layer 5, dt = 800 years, rho1 advection, rhobc diff')
#ax.plot(disp_3d_DG0_nz10_rho1adv_bcdiff[:, 0], disp_3d_DG0_nz10_rho1adv_bcdiff[:, 1], '*', color='blue',markevery=1, label='3d dx = 5 km (refined), DG0 cells per layer 10, dt = 800 years, rho1 advection, rhobc diff')
#ax.plot(disp_3d_DG0_nz20_rho1adv_bcdiff[:, 0], disp_3d_DG0_nz20_rho1adv_bcdiff[:, 1], '*', color='black',markevery=1, label='3d dx = 5 km (refined), DG0 cells per layer 20, dt = 800 years, rho1 advection, rhobc diff')

#ax.plot(disp_3d_DG0_nz5_rho1adv_bcdiff_nofs[:, 0], disp_3d_DG0_nz5_rho1adv_bcdiff_nofs[:, 1], '+', color='green',markevery=1, label='3d dx = 5 km (refined), DG0 cells per layer 5, dt = 800 years, rho1 advection, rhobc diff, nofs')
# P1DG
#ax.plot(disp_3d_DG0_nz5_rho1adv_bcdiff_nofs_p1dg[:, 0], disp_3d_DG0_nz5_rho1adv_bcdiff_nofs_p1dg[:, 1], '--', color='green',markevery=1, label='3d dx = 5 km (refined), DG0 cells per layer 5, dt = 800 years, rho1 advection, rhobc diff, nofs, P1dg')
#ax.plot(disp_3d_DG0_nz10_rho1adv_bcdiff_nofs_p1dg[:, 0], disp_3d_DG0_nz10_rho1adv_bcdiff_nofs_p1dg[:, 1], '--', color='blue',markevery=1, label='3d dx = 5 km (refined), DG0 cells per layer 10, dt = 800 years, rho1 advection, rhobc diff, nofs, P1dg')
#ax.plot(disp_3d_DG0_nz20_rho1adv_bcdiff_nofs_p1dg[:, 0], disp_3d_DG0_nz20_rho1adv_bcdiff_nofs_p1dg[:, 1], '--', color='black',markevery=1, label='3d dx = 5 km (refined), DG0 cells per layer 20, dt = 800 years, rho1 advection, rhobc diff, nofs, P1dg')


# 3d DG0 ibp interior facet hydprestress rho1 jan 2025
#ax.plot(disp_3d_DG0_ibp_nz5_icetanh1[:, 0]-800, disp_3d_DG0_ibp_nz5_icetanh1[:, 1], '--', color='green',markevery=1, label='3d dx = 5 km (refined), DG0 cells per layer 5, dt = 800 years, ibp/intfacet icetahn1km')
#ax.plot(disp_3d_DG0_ibp_nz8_icetanh1[:, 0]-800, disp_3d_DG0_ibp_nz8_icetanh1[:, 1], '--', color='orange',markevery=1, label='3d dx = 5 km (refined), DG0 cells per layer 8, dt = 800 years, ibp/intfacet icetahn1km')
#ax.plot(disp_3d_DG0_ibp_nz40_icetanh1[:, 0]-800, disp_3d_DG0_ibp_nz40_icetanh1[:, 1], '--', color='purple',markevery=1, label='3d dx = 5 km (refined), DG0 cells per layer 40, dt = 800 years, all ibp, delta rhofs rho1dst')

# 3d DG0 ibp interior facet hydprestress rho1 jan 2025 icetanh2
#ax.plot(disp_3d_DG0_ibp_nz5_icetanh2[:, 0], disp_3d_DG0_ibp_nz5_icetanh2[:, 1], 'o', color='green',markevery=1, label='3d dx = 5 km (refined), DG0 cells per layer 5, dt = 800 years, ibp/intfacet icetahn2km')
#ax.plot(disp_3d_DG0_ibp_nz8_icetanh2[:, 0], disp_3d_DG0_ibp_nz8_icetanh2[:, 1], 'o', color='orange',markevery=1, label='3d dx = 5 km (refined), DG0 cells per layer 8, dt = 800 years, ibp/intfacet icetahn2km')
#ax.plot(disp_3d_DG0_ibp_nz20_icetanh2[:, 0]-800, disp_3d_DG0_ibp_nz20_icetanh2[:, 1], 'o', color='black',markevery=1, label='3d dx = 5 km (refined), DG0 cells per layer 20, dt = 800 years, ibp/intfacet icetahn2km')
#ax.plot(disp_3d_DG0_ibp_nz40_icetanh2[:, 0], disp_3d_DG0_ibp_nz40_icetanh2[:, 1], 'o', color='purple',markevery=1, label='3d dx = 5 km (refined), DG0 cells per layer 40, dt = 800 years, ibp/intfacet icetahn2km')

# 3d DG0 ibp interior facet hydprestress rho1 with explicit displacemacement for rho1! , run on 25th jan 2025 icetanh2 plotted 28/1/25
#ax.plot(disp_3d_DG0_ibp_nz40_icetanh1_dt10000[:, 0]-10000, disp_3d_DG0_ibp_nz40_icetanh1_dt10000[:, 1], '--o', color='grey',markevery=1, label='3d dx = 5 km (refined), DG0 cells per layer 40, dt = 10000 years, all ibp delta rho fs rho1dst')
#ax.plot(disp_3d_DG0_ibp_nz40_icetanh1_dt5000[:, 0]-5000, disp_3d_DG0_ibp_nz40_icetanh1_dt5000[:, 1], '--v', color='brown',markevery=1, label='3d dx = 5 km (refined), DG0 cells per layer 40, dt = 5000 years, ibp/intfacet all ibp delta rho fs rho1dst')
#ax.plot(disp_3d_DG0_ibp_nz40_icetanh1_dt1000[:, 0]-1000, disp_3d_DG0_ibp_nz40_icetanh1_dt1000[:, 1], '--x', color='purple',markevery=1, label='3d dx = 5 km (refined), DG0 cells per layer 40, dt = 1000 years, all ibp delta rho fs rho1dst')
#ax.plot(disp_3d_DG0_ibp_nz40_icetanh1_dt400[:, 0]-400, disp_3d_DG0_ibp_nz40_icetanh1_dt400[:, 1], '--^', color='red',markevery=1, label='3d dx = 5 km (refined), DG0 cells per layer 40, dt = 400 years, all ibp delta rho fs rho1dst')
#ax.plot(disp_3d_DG0_ibp_nz40_icetanh1_dt200[:, 0]-200, disp_3d_DG0_ibp_nz40_icetanh1_dt200[:, 1], '--+', color='orange',markevery=1, label='3d dx = 5 km (refined), DG0 cells per layer 40, dt = 200 years, all ibp delta rho fs rho1dst')

# 3d DG0 ibp interior facet hydprestress rho1 with implicit displacemacement for rho1 (fails symmetric check for nz=10/layer and dt >5000a)! , run on 25th jan 2025 icetanh2 plotted 28/1/25
#ax.plot(disp_3d_DG0_ibp_nz40_icetanh1_dt200_impdisp[:, 0]-200, disp_3d_DG0_ibp_nz40_icetanh1_dt200_impdisp[:, 1], '+', color='orange',markevery=1, label='3d dx = 5 km (refined), DG0 cells per layer 40, dt = 200 years, ibp/intfacet icetahn1km, imp disp rho1')
#ax.plot(disp_3d_DG0_ibp_nz40_icetanh1_dt400_impdisp[:, 0]-400, disp_3d_DG0_ibp_nz40_icetanh1_dt400_impdisp[:, 1], 'x', color='orange',markevery=1, label='3d dx = 5 km (refined), DG0 cells per layer 40, dt = 400 years, ibp/intfacet icetahn1km, imp disp rho1')
#ax.plot(disp_3d_DG0_ibp_nz40_icetanh1_dt800_impdisp[:, 0]-800, disp_3d_DG0_ibp_nz40_icetanh1_dt800_impdisp[:, 1], '--', color='orange',markevery=1, label='3d dx = 5 km (refined), DG0 cells per layer 40, dt = 800 years, ibp/intfacet icetahn1km, imp disp rho1')
#ax.plot(disp_3d_DG0_ibp_nz40_icetanh1_dt1000_impdisp[:, 0]-1000, disp_3d_DG0_ibp_nz40_icetanh1_dt1000_impdisp[:, 1], '^', color='orange',markevery=1, label='3d dx = 5 km (refined), DG0 cells per layer 40, dt = 1000 years, ibp/intfacet icetahn1km, imp disp rho1')


# 3d DG0 ibp no free surface, rho1 ibp but no top surface. run on 31.01.25 plotted 06.02.25
#ax.plot(disp_3d_DG0_ibp_nz5_nofs_norho1dst[:, 0]-1000, disp_3d_DG0_ibp_nz5_nofs_norho1dst[:, 1], 'o', color='green',markevery=1, label='3d dx = 5 km (refined), DG0 cells per layer 5, dt = 1000 years, all ibp, no freesurface, norho1 dstop')
#ax.plot(disp_3d_DG0_ibp_nz10_nofs_norho1dst[:, 0]-1000, disp_3d_DG0_ibp_nz10_nofs_norho1dst[:, 1], 'o', color='blue',markevery=1, label='3d dx = 5 km (refined), DG0 cells per layer 5, dt = 1000 years, all ibp, no freesurface, norho1 dstop')
#ax.plot(disp_3d_DG0_ibp_nz20_nofs_norho1dst[:, 0]-1000, disp_3d_DG0_ibp_nz20_nofs_norho1dst[:, 1], 'o', color='black',markevery=1, label='3d dx = 5 km (refined), DG0 cells per layer 5, dt = 1000 years, all ibp, no freesurface, norho1 dstop')
#ax.plot(disp_3d_DG0_ibp_nz40_nofs_norho1dst[:, 0]-1000, disp_3d_DG0_ibp_nz40_nofs_norho1dst[:, 1], 'o', color='purple',markevery=1, label='3d dx = 5 km (refined), DG0 cells per layer 5, dt = 1000 years, all ibp, no freesurface, norho1 dstop')

# 3d DG0 ibp fs rho0, no rho1 run on 31.01.25 plotted 06.02.25
#ax.plot(disp_3d_DG0_ibp_nz5_fsrho0_norho1[:, 0]-1000, disp_3d_DG0_ibp_nz5_fsrho0_norho1[:, 1], '+', color='green',markevery=1, label='3d dx = 5 km (refined), DG0 cells per layer 5, dt = 1000 years, prestressadv ibp, freesurface rho0, norho1 ')
#ax.plot(disp_3d_DG0_ibp_nz10_fsrho0_norho1[:, 0]-1000, disp_3d_DG0_ibp_nz10_fsrho0_norho1[:, 1], '+', color='blue',markevery=1, label='3d dx = 5 km (refined), DG0 cells per layer 10, dt = 1000 years, prestressadv ibp, freesurface rho0, norho1')
#ax.plot(disp_3d_DG0_ibp_nz20_fsrho0_norho1[:, 0]-1000, disp_3d_DG0_ibp_nz20_fsrho0_norho1[:, 1], '+', color='black',markevery=1, label='3d dx = 5 km (refined), DG0 cells per layer 20, dt = 1000 years, prestressadv all ibp, freesurface rho0, norho1')
#ax.plot(disp_3d_DG0_ibp_nz40_fsrho0_norho1[:, 0]-1000, disp_3d_DG0_ibp_nz40_fsrho0_norho1[:, 1], '+', color='purple',markevery=1, label='3d dx = 5 km (refined), DG0 cells per layer 40, dt = 1000 years, prestressadv ibp, freesurface rho0, norho1')


# 3d DG0 no ibp, just prestressadv no rho1
#ax.plot(disp_3d_DG0_noibp_nz5_jan25_justprestressadv_norho1[:, 0]-1000, disp_3d_DG0_noibp_nz5_jan25_justprestressadv_norho1[:, 1], '--', color='green',markevery=1, label='3d dx = 5 km (refined), DG0 cells per layer 5, dt = 1000 years, no ibp, prestressadv, norho1 ')

# 3d P1 no ibp, just prestressadv,  rho1
#ax.plot(disp_3d_P1_noibp_nz5_feb25_prestressadv_rho1[:, 0]-1000, disp_3d_P1_noibp_nz5_feb25_prestressadv_rho1[:, 1], '^', color='green',markevery=1, label='3d dx = 5 km (refined), P1 cells per layer 5, dt = 1000 years, no ibp, prestressadv, rho1 ')
#ax.plot(disp_3d_P1_noibp_nz10_feb25_prestressadv_rho1[:, 0]-1000, disp_3d_P1_noibp_nz10_feb25_prestressadv_rho1[:, 1], '^', color='blue',markevery=1, label='3d dx = 5 km (refined), P1 cells per layer 10, dt = 1000 years, no ibp, prestressadv, rho1 ')
#ax.plot(disp_3d_P1_noibp_nz20_feb25_prestressadv_rho1[:, 0]-1000, disp_3d_P1_noibp_nz20_feb25_prestressadv_rho1[:, 1], '^', color='black',markevery=1, label='3d dx = 5 km (refined), P1 cells per layer 20, dt = 1000 years, no ibp, prestressadv, rho1 ')
#ax.plot(disp_3d_P1_noibp_nz40_feb25_prestressadv_rho1[:, 0]-1000, disp_3d_P1_noibp_nz40_feb25_prestressadv_rho1[:, 1], '^', color='purple',markevery=1, label='3d dx = 5 km (refined), P1 cells per layer 40, dt = 1000 years, no ibp, prestressadv, rho1 ')
#ax.plot(disp_3d_P1_noibp_nz40_feb25_prestressadv_rho1_dt500[:, 0]-500, disp_3d_P1_noibp_nz40_feb25_prestressadv_rho1_dt500[:, 1], '--', color='purple',markevery=1, label='3d dx = 5 km (refined), P1 cells per layer 40, dt = 500 years, no ibp, prestressadv, rho1 ')


## 3D P1 ibp, freesurface rho0, rho1
#ax.plot(disp_3d_P1_ibp_nz5_feb25_fsrho0_rho1[:, 0]-1000, disp_3d_P1_ibp_nz5_feb25_fsrho0_rho1[:, 1], 'v', color='green',markevery=1, label='3d dx = 5 km (refined), P1 cells per layer 5, dt = 1000 years, ibp, free surface rho0, rho1 ')
#ax.plot(disp_3d_P1_ibp_nz10_feb25_fsrho0_rho1[:, 0]-1000, disp_3d_P1_ibp_nz10_feb25_fsrho0_rho1[:, 1], 'v', color='blue',markevery=1, label='3d dx = 5 km (refined), P1 cells per layer 10, dt = 1000 years, ibp, free surface rho0, rho1 ')
#ax.plot(disp_3d_P1_ibp_nz20_feb25_fsrho0_rho1[:, 0]-1000, disp_3d_P1_ibp_nz20_feb25_fsrho0_rho1[:, 1], 'v', color='black',markevery=1, label='3d dx = 5 km (refined), P1 cells per layer 20, dt = 1000 years, ibp, free surface rho0, rho1 ')
#ax.plot(disp_3d_P1_ibp_nz40_feb25_fsrho0_rho1[:, 0]-1000, disp_3d_P1_ibp_nz40_feb25_fsrho0_rho1[:, 1], 'v', color='purple',markevery=1, label='3d dx = 5 km (refined), P1 cells per layer 40, dt = 1000 years, ibp, free surface rho0, rho1 ')
#ax.plot(disp_3d_P1_ibp_nz80_feb25_fsrho0_rho1[:, 0]-1000, disp_3d_P1_ibp_nz80_feb25_fsrho0_rho1[:, 1], 'v', color='red',markevery=1, label='3d dx = 5 km (refined), P1 cells per layer 80, dt = 1000 years, ibp, free surface rho0, rho1 ')

# 3d P1 ibp, freesurface rho0, rho1 old mesh
#ax.plot(disp_3d_P1_ibp_nz20_feb25_fsrho0_rho1_oldmesh[:, 0]-1000, disp_3d_P1_ibp_nz20_feb25_fsrho0_rho1_oldmesh[:, 1], 'v', color='green',markevery=1, label='3d dx = 5 km (refined), P1 20 cells total (old mesh), dt = 1000 years, ibp, free surface rho0, rho1 ')
#ax.plot(disp_3d_P1_ibp_nz40_feb25_fsrho0_rho1_oldmesh[:, 0]-1000, disp_3d_P1_ibp_nz40_feb25_fsrho0_rho1_oldmesh[:, 1], 'v', color='blue',markevery=1, label='3d dx = 5 km (refined), P1 20 cells total (old mesh), dt = 1000 years, ibp, free surface rho0, rho1 ')
#ax.plot(disp_3d_P1_ibp_nz80_feb25_fsrho0_rho1_oldmesh[:, 0]-1000, disp_3d_P1_ibp_nz80_feb25_fsrho0_rho1_oldmesh[:, 1], 'v', color='black',markevery=1, label='3d dx = 5 km (refined), P1 20 cells total (old mesh), dt = 1000 years, ibp, free surface rho0, rho1 ')
#ax.plot(disp_3d_P1_ibp_nz160_feb25_fsrho0_rho1_oldmesh[:, 0]-1000, disp_3d_P1_ibp_nz160_feb25_fsrho0_rho1_oldmesh[:, 1], 'v', color='purple',markevery=1, label='3d dx = 5 km (refined), P1 20 cells total (old mesh), dt = 1000 years, ibp, free surface rho0, rho1 ')
#ax.plot(disp_3d_P1_ibp_nz320_feb25_fsrho0_rho1_oldmesh[:, 0]-1000, disp_3d_P1_ibp_nz320_feb25_fsrho0_rho1_oldmesh[:, 1], 'v', color='red',markevery=1, label='3d dx = 5 km (refined), P1 20 cells total (old mesh), dt = 1000 years, ibp, free surface rho0, rho1 ')

# 3d internal variable, nz comparison late feb/march 2025
#ax.plot(disp_3d_intvar_dt1ka_k1e13_nz1_mar25[:, 0], disp_3d_intvar_dt1ka_k1e13_nz1_mar25[:, 1], 'o', color='red',markevery=1, label='3d dx = 5 km (refined), DG 1 cell per layer, dt = 1000 years, internal variable')
#ax.plot(disp_3d_intvar_dt1ka_k1e13_nz2_mar25[:, 0], disp_3d_intvar_dt1ka_k1e13_nz2_mar25[:, 1], 'o', color='purple',markevery=1, label='3d dx = 5 km (refined), DG 2 cells per layer, dt = 1000 years, internal variable')
#ax.plot(disp_3d_intvar_dt1ka_k1e13_nz4_mar25[:, 0], disp_3d_intvar_dt1ka_k1e13_nz4_mar25[:, 1], 'o', color='yellow',markevery=1, label='3d dx = 5 km (refined), DG 4 cells per layer, dt = 1000 years, internal variable')
#ax.plot(disp_3d_intvar_dt1ka_k1e13_nz5_mar25[:, 0], disp_3d_intvar_dt1ka_k1e13_nz5_mar25[:, 1], 'o', color='green',markevery=1, label='3d dx = 5 km (refined), DG 5 cells per layer, dt = 1000 years, internal variable')
#ax.plot(disp_3d_intvar_dt1ka_k1e13_nz8_mar25[:, 0], disp_3d_intvar_dt1ka_k1e13_nz8_mar25[:, 1], 'o', color='orange',markevery=1, label='3d dx = 5 km (refined), DG 8 cells per layer, dt = 1000 years, internal variable')
#ax.plot(disp_3d_intvar_dt1ka_k1e13_nz10_mar25[:, 0], disp_3d_intvar_dt1ka_k1e13_nz10_mar25[:, 1], 'o', color='blue',markevery=1, label='3d dx = 5 km (refined), DG 10 cells per layer, dt = 1000 years, internal variable')
#ax.plot(disp_3d_intvar_dt1ka_k1e13_nz20_mar25[:, 0], disp_3d_intvar_dt1ka_k1e13_nz20_mar25[:, 1], 'o', color='black',markevery=1, label='3d dx = 5 km (refined), DG 20 cells per layer, dt = 1000 years, internal variable')


# 3d internal variable, nz =5, bulk comparison late feb/march 2025
#ax.plot(disp_3d_intvar_dt1ka_nz5_k1e11_mar25[:, 0], disp_3d_intvar_dt1ka_nz5_k1e11_mar25[:, 1], 'x', color='green',markevery=1, label='3d dx = 5 km (refined), DG 5 cells per layer, dt = 1000 years, internal variablem bulk = 1e11Pa')
#ax.plot(disp_3d_intvar_dt1ka_nz5_k1e12_mar25[:, 0], disp_3d_intvar_dt1ka_nz5_k1e12_mar25[:, 1], '^', color='green',markevery=1, label='3d dx = 5 km (refined), DG 5 cells per layer, dt = 1000 years, internal variablem bulk = 1e12Pa')
#ax.plot(disp_3d_intvar_dt1ka_nz5_k1e13_mar25[:, 0], disp_3d_intvar_dt1ka_nz5_k1e13_mar25[:, 1], 'o', color='green',markevery=1, label='3d dx = 5 km (refined), DG 5 cells per layer, dt = 1000 years, internal variablem bulk = 1e13Pa')
#ax.plot(disp_3d_intvar_dt1ka_nz5_k1e14_mar25[:, 0], disp_3d_intvar_dt1ka_nz5_k1e14_mar25[:, 1], '+', color='green',markevery=1, label='3d dx = 5 km (refined), DG 5 cells per layer, dt = 1000 years, internal variablem bulk = 1e14Pa')

# 3d internal variable, dt comparison late feb/march 2025
#ax.plot(disp_3d_intvar_nz10_k1e13_dt500a_mar25[:, 0], disp_3d_intvar_nz10_k1e13_dt500a_mar25[:, 1], 'x--', color='blue',markevery=1, label='3d dx = 5 km (refined), DG 10 cell per layer, dt = 500 years, internal variable')
#ax.plot(disp_3d_intvar_nz10_k1e13_dt1000a_mar25[:, 0], disp_3d_intvar_nz10_k1e13_dt1000a_mar25[:, 1], 'o--', color='black',markevery=1, label='3d dx = 5 km (refined), DG 10 cell per layer, dt = 1000 years, internal variable')
#ax.plot(disp_3d_intvar_nz10_k1e13_dt2000a_mar25[:, 0], disp_3d_intvar_nz10_k1e13_dt2000a_mar25[:, 1], '+--', color='red',markevery=1, label='3d dx = 5 km (refined), DG 10 cell per layer, dt = 2000 years, internal variable')
#ax.plot(disp_3d_intvar_nz10_k1e13_dt5000a_mar25[:, 0], disp_3d_intvar_nz10_k1e13_dt5000a_mar25[:, 1], 'v--', color='purple',markevery=1, label='3d dx = 5 km (refined), DG 10 cell per layer, dt = 5000 years, internal variable')
#ax.plot(disp_3d_intvar_nz10_k1e13_dt10000a_mar25[:, 0], disp_3d_intvar_nz10_k1e13_dt10000a_mar25[:, 1], '^--', color='green',markevery=1, label='3d dx = 5 km (refined), DG 10 cell per layer, dt = 10000 years, internal variable')

# 3d internal variable check non dimensional vs dimensional 
#ax.plot(disp_3d_intvar_nz10_k1e13_dt1000a_mar25[:, 0], disp_3d_intvar_nz10_k1e13_dt1000a_mar25[:, 1], 'o', color='blue',markevery=1, label='3d dx = 5 km (refined), DG 10 cell per layer, dt = 1000 years, internal variable')
#ax.plot(disp_3d_intvar_nondim_k1e13_dt1ka_nz10_dx5_mar25[:, 0], disp_3d_intvar_nondim_k1e13_dt1ka_nz10_dx5_mar25[:, 1], 'x', color='green',markevery=1, label='3d dx = 5 km (refined), DG 10 cell per layer, dt = 1000 years, internal variable, nondimensional')

# 3d internal variabl nondim dx comparison plot march 14th march 2025
#ax.plot(disp_3d_intvar_nondim_k1e13_dt1ka_nz10_dx40_mar25[:, 0], disp_3d_intvar_nondim_k1e13_dt1ka_nz10_dx40_mar25[:, 1], '+', color='red',markevery=1, label='3d dx = 40 km (refined), DG 10 cell per layer, dt = 1000 years, internal variable')
#ax.plot(disp_3d_intvar_nondim_k1e13_dt1ka_nz10_dx20_mar25[:, 0], disp_3d_intvar_nondim_k1e13_dt1ka_nz10_dx20_mar25[:, 1], '+', color='black',markevery=1, label='3d dx = 20 km (refined), DG 10 cell per layer, dt = 1000 years, internal variable')
#ax.plot(disp_3d_intvar_nondim_k1e13_dt1ka_nz10_dx10_mar25[:, 0], disp_3d_intvar_nondim_k1e13_dt1ka_nz10_dx10_mar25[:, 1], '+', color='green',markevery=1, label='3d dx = 10 km (refined), DG 10 cell per layer, dt = 1000 years, internal variable')
#ax.plot(disp_3d_intvar_nondim_k1e13_dt1ka_nz10_dx5_mar25[:, 0], disp_3d_intvar_nondim_k1e13_dt1ka_nz10_dx5_mar25[:, 1], '+', color='blue',markevery=1, label='3d dx = 5 km (refined), DG 10 cell per layer, dt = 1000 years, internal variable, nondimensional')


# 3d internal variable nondim check 1000x bulk
ax.plot(disp_3d_intvar_nondim_k1e13_dt1ka_nz10_dx5_mar25[:, 0], disp_3d_intvar_nondim_k1e13_dt1ka_nz10_dx5_mar25[:, 1], 'x', color='blue',markevery=1, label='3d dx = 5 km (refined), DG 10 cell per layer, dt = 1000 years, internal variable, nondimensional, k=100mu')
ax.plot(disp_3d_intvar_nondim_k1e14_dt1ka_nz10_dx5_mar25[:, 0], disp_3d_intvar_nondim_k1e14_dt1ka_nz10_dx5_mar25[:, 1], '--', color='black',markevery=1, label='3d dx = 5 km (refined), DG 10 cell per layer, dt = 1000 years, internal variable, nondimensional, k=1000mu')

#ax.plot(disp_3d_P1_nz20_g_nofsrho1_norho1[:, 0], disp_3d_P1_nz20_g_nofsrho1_norho1[:, 1], '--', color='red', label='3d dx = 5 km (refined), P1 cells per layer 20, dt = 50 years, tanh width = 0 km, modifid g =9.815, norho1')
# default no tanh, log10viscoisty
#ax.plot(disp_3d_nz80default_notanh_log10visc[:, 0], disp_3d_nz80default_notanh_log10visc[:, 1], '--', markevery=20, color='black', label='3d dx = 5 km (refined), nz = 80, dt = 50 years, log10viscosity')
#ax.plot(disp_3d_nz80default_notanh_normalvisc[:, 0], disp_3d_nz80default_notanh_normalvisc[:, 1], '--', markevery=20, color='orange', label='3d dx = 5 km (refined), nz = 80, dt = 50 years, normal viscosity')
# dt
#ax.plot(disp_3d_dx5_nz80_dt800[:, 0], disp_3d_dx5_nz80_dt800[:, 1], '-', label='3d dx = 5 km (refined), nz = 80, dt = 800 years')
#ax.plot(disp_3d_dx5_nz80_dt400[:, 0], disp_3d_dx5_nz80_dt400[:, 1], '-', label='3d dx = 5 km (refined), nz = 80, dt = 400 years')
#ax.plot(disp_3d_dx5_nz80_dt200[:, 0], disp_3d_dx5_nz80_dt200[:, 1], '-', label='3d dx = 5 km (refined), nz = 80, dt = 200 years')
#ax.plot(disp_3d_dx5_nz80_dt100[:, 0], disp_3d_dx5_nz80_dt100[:, 1], '-', label='3d dx = 5 km (refined), nz = 80, dt = 100 years')
#ax.plot(disp_3d_dx5_nz80_dt50[:, 0], disp_3d_dx5_nz80_dt50[:, 1], '-', label='3d dx = 5 km (refined), nz = 80, dt = 50 years (default)')

# Refined box
#ax.plot(disp_3d_dxz20_dt50[:, 0], disp_3d_dxz20_dt50[:, 1], 'x', markevery=20, label='3d dx = dz = 20 km (refined) dt = 50 years')
#ax.plot(disp_3d_dxz10_dt50[:, 0], disp_3d_dxz10_dt50[:, 1], '--o', markevery=20, color='blue', label='3d dx = dz = 10 km (refined) dt = 50 years')
#ax.plot(disp_3d_dxz6pt25_dt50[:, 0], disp_3d_dxz6pt25_dt50[:, 1], '--o', markevery=20, color='green', label='3d dx = dz = 6.25 km (refined) dt = 50 years')
#ax.plot(disp_3d_dxz5_dt50[:, 0], disp_3d_dxz5_dt50[:, 1], '--o', markevery=20, color='black', label='3d dx = dz = 5 km (refined) dt = 50 years')
#ax.plot(disp_3d_dxz2pt5_dt50[:, 0], disp_3d_dxz2pt5_dt50[:, 1], '--o', markevery=20, color='red', label='3d dx = dz = 2.5 km (refined) dt = 50 years')

#
#print("length of old vom", len(disp_2d_old[0]))
#print("length of old vom new FD ", len(disp_2d_old_newFD[0]))
#print("length of old vom new FD (check today)", len(disp_2d_old_newFD_testing[0]))
#print("length of new vom", len(disp_2d_new_testing[0]))


print("hobart length ", len(disp_oldFD_long_gradmesh_TDG2_drhog_rho1g_strong[index_long_gradmesh_TDG2_drhog_rho1g_strong, 1:]))

#matplotlib.rc('font', **font)
plt.rcParams.update({'font.size': 30})

font = {'size': 20}
 
# using rc function
plt.rc('font', **font)
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
#ax.set_xlim([0, 1000])
#ax.set_ylim([-0.5, 0])
ax.set_xlabel('Time (years)', fontsize='30')
ax.set_ylabel('Maximum vertical displacement (m)', fontsize='30')
ax.grid(True)
ax.legend()
fig.savefig(f'17.03.25_gadopt_3d_weerdesteijn_internalvariable_dim_bulk1e14_nz10_dx5_dt1ka.png')
#plt.show()
ax.set_xlim([70e3, 110e3])
ax.set_ylim([-80, -45])
fig.savefig(f'17.03.25_gadopt_3d_weerdesteijn_internalvariable_dim_bulk1e14_nz10_dx5_dt1ka_zoom_peak.png')

ax.set_xlim([85e3, 110e3])
ax.set_ylim([-70, -5])
fig.savefig(f'17.03.25_gadopt_3d_weerdesteijn_internalvariable_dim_bulk1e14_nz10_dx5_dt1ka_zoom_end.png')

ax.set_xlim([-5e2, 20e3])
ax.set_ylim([-20, 1])
fig.savefig(f'17.03.25_gadopt_3d_weerdesteijn_internalvariable_dim_bulk1e14_nz10_dx5_dt1ka_zoom_start.png')

print("time", time50gradmesh_TDG2_drhog_rho1g_strong[1800])
print("static mesh", disp_oldFD_long_gradmesh_TDG2_drhog_rho1g_strong[index_long_gradmesh_TDG2_drhog_rho1g_strong, 1800])
print("move mesh", disp_oldFD_long_gradmesh_TDG2_drhog_rho1_move[index_long_gradmesh_TDG2_drhog_move, 1800])
#plt.show()
'''
plt.figure()
plt.plot(1e-3*distance_fromcentre, displacement_40[:, -1], label='surface id off prezhong') 
plt.plot(1e-3*distance_fromcentre, displacement[:, -1], label='surface id off prezhong 160 layers') 
plt.plot(1e-3*distance_fromcentre, displacement_rhog[:, -1], label='surface id off prezhong change rhog') 
plt.plot(1e-3*distance_fromcentre, displacement_zhong[:, -1], label='surface id off zhong') 
plt.plot(1e-3*distance_fromcentre, displacement_zhong_topid_nodrhog[:, -1], label='surface id on zhong no drhog') 
plt.plot(1e-3*distance_fromcentre, displacement_zhong_topid_nodrhog_80[:, -1], label='surface id on zhong no drhog 80 layers') 
#plt.plot(1e-3*distance_fromcentre, displacement_zhong_topid[:, -1], label='surface id on') 
#plt.plot(1e-3*distance_fromcentre, displacement_zhong_topid_prestress[:, -1], label='neg stress') 
#plt.plot(1e-3*distance_fromcentre, displacement_zhong_topid_prestress_pos[:, -1], label='pos stress') 
#plt.plot(1e-3*distance_fromcentre, displacement_zhong_topid_prestress_pos_nodrhog[:, -1], label='pos stress no delta rhog') 
#plt.plot(1e-3*distance_fromcentre, displacement_zhong_topid_prestress_pos_nodrhog_160[:, -1], label='pos stress no delta rhog 160') 
#plt.plot(115, -0.6698, 'x')
#plt.plot(time[1:5], actual_aspect, 'x')
plt.legend()
plt.show() '''
