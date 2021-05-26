BEGIN{FS = "."} 
{    
   for(i=1; i<=NF; i++){
        if($i ~ /,Irmaos/)
               {rela["Irmãos"]++};
        

        if($i ~ /,Irmao/)
               {rela["Irmao"]++};

        if($i ~ /,Tio Paterno/)
               {rela["Tio Patero"]++}
        

        if($i ~ /,Tio Materno/)
              {rela["Tio Materno"]++};
        

        if($i ~ /,Pai/)
              {rela["Pai"]++};

        if($i ~ /,Pais/)
              {rela["Pais"]++};

        if($i ~ /,Sobrinho Materno/)
              {rela["Sobrinho Materno"]++};

        if($i ~ /,Sobrinho Paterno/)
              {rela["Sobrinho Paterno"]++};

        if($i ~ /,Primo/)
              {rela["Primo"]++};

        if($i ~ /,Avo Materno/)
              {rela["Avo Materno"]++};

        if($i ~ /,Avo Paterno/)
              {rela["Avo Paterno"]++};

        if($i ~ /,Tio Avo Materno/)
              {rela["Tio Avo Materno"]++};

        if($i ~ /,Tio Avo Paterno/)
              {rela["Tio Avo Paterno"]++};

        if($i ~ /,Neto Paterno/)
              {rela["Neto Paterno"]++};

        if($i ~ /,Neto Materno/)
              {rela["Neto Materno"]++};

        if($i ~ /,Sobrinho Bisneto Paterno/)
              {rela["Sobrinho Bisneto Paterno"]++};
        
        if($i ~ /,Sobrinho Bisneto Materno/)
              {rela["Sobrinho Bisneto Materno"]++};
    }
}

END {
     for (r in rela) {print "Da relação  " r "  há  " rela[r] "  relações"}
     }
