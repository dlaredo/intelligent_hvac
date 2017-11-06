function startDamadicsSimulation2()


            DGenBlockAddress = 'RDataGeneration/RDGen';

            initModel();

            if exist('lastDateTime.mat', 'file') == 2
                load('lastDateTime.mat', 'lastSimulationDateTime')
            else
                lastSimulationDateTime = datetime();
                save('lastDateTime.mat', 'lastSimulationDateTime');
            end

            assignin('base', 'lastSimulationDateTime', lastSimulationDateTime+seconds(5));

            set_param(strcat(DGenBlockAddress, '/Disable simulation'), 'value', '0');
            fprintf(2, 'starting simulation');
            sim('RDataGeneration');

            clc;
    
end