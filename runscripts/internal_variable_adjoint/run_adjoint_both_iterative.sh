
mpiexec -np 8 python adjoint_both_iterative.py --dt_years 50 --ncells 360 --DG0_layers 20 --controls ice --optional_name "step0" > 17.04.25_iterative_adjoint_velscale1e-9_ctypeice_step0

control_check_path="/data/viscoelastic/internal_variable_adjoint/adjoint/"

for i in $(seq 1 10);
do 
	echo "Step ${i}"
	iold=$((i-1))

	if [ $((i%2)) -eq 0 ]
	then
		ctype="ice"
		ctype_old="viscosity"
	else
		ctype="viscosity"
		ctype_old="ice"
	fi
	echo $ctype
	control_check_name="${control_check_path}adjoint-cylinder-2d-internalvariable-ctype${ctype_old}-step${iold}_controls.h5"

	echo $control_check_name
	
	mpiexec -np 8 python adjoint_both_iterative.py --dt_years 50 --ncells 360 --DG0_layers 20 --controls $ctype --optional_name "step${i}" --ice_checkpoint $control_check_name --viscosity_checkpoint $control_check_name > 17.04.25_iterative_adjoint_velscale1e-9_ctype${ctype}_step${i}
done

